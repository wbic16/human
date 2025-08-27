#include <exception>
#include <iosfwd>
#include <iostream>
#include <string>
#include <vector>

// Experiments in compression

struct CacheLine
{
  uint64_t b0{};
  uint64_t b1{};
  uint64_t b2{};
  uint64_t b3{};
  uint64_t b4{};
  uint64_t b5{};
  uint64_t b6{};
  uint64_t b7{};
};
std::ostream& operator<<(std::ostream& o, const CacheLine& c)
{
  o << "CL: " << std::hex << c.b0
    << ", " << c.b1
    << ", " << c.b2
    << ", " << c.b3
    << ", " << c.b4
    << ", " << c.b5
    << ", " << c.b6
    << ", " << c.b7;
  return o;
}
static_assert(sizeof(CacheLine) == 64, "CacheLine must be 512 bits on 64-bit machines.");

enum Register : uint64_t
{
  r0, r1, r2, r3, r4, r5, r6, r7,
  r8, r9, ra, rb, rc, rd, re, rf
};

Register valueToRegister(uint64_t value)
{
  uint64_t test = (0xf000000000000000 & value) >> 60;
  return static_cast<Register>(test);
}

Register cacheLineToRegister(const CacheLine& c)
{
  return valueToRegister(c.b0);
}

std::ostream& operator<<(std::ostream& o, const Register& r)
{
  switch (r)
  {
    case r0: o << "r0"; break;
    case r1: o << "r1"; break;
    case r2: o << "r2"; break;
    case r3: o << "r3"; break;
    case r4: o << "r4"; break;
    case r5: o << "r5"; break;
    case r6: o << "r6"; break;
    case r7: o << "r7"; break;
    case r8: o << "r8"; break;
    case r9: o << "r9"; break;
    case ra: o << "ra"; break;
    case rb: o << "rb"; break;
    case rc: o << "rc"; break;
    case rd: o << "rd"; break;
    case re: o << "re"; break;
    case rf: o << "rf"; break;
    default: break;
  }
  return o;
}

std::string tester(uint64_t value, Register expected)
{
  return valueToRegister(value) == expected ? "OK" : "Failed";
}
std::string test_r0() { return tester(0x0123456789345678, Register::r0); }
std::string test_r1() { return tester(0x1123456789345678, Register::r1); }
std::string test_r2() { return tester(0x2123456789345678, Register::r2); }
std::string test_r3() { return tester(0x3123456789345678, Register::r3); }
std::string test_r4() { return tester(0x4123456789345678, Register::r4); }
std::string test_r5() { return tester(0x5123456789345678, Register::r5); }
std::string test_r6() { return tester(0x6123456789345678, Register::r6); }
std::string test_r7() { return tester(0x7123456789345678, Register::r7); }
std::string test_r8() { return tester(0x8123456789345678, Register::r8); }
std::string test_r9() { return tester(0x9123456789345678, Register::r9); }
std::string test_ra() { return tester(0xa123456789345678, Register::ra); }
std::string test_rb() { return tester(0xb123456789345678, Register::rb); }
std::string test_rc() { return tester(0xc123456789345678, Register::rc); }
std::string test_rd() { return tester(0xd123456789345678, Register::rd); }
std::string test_re() { return tester(0xe123456789345678, Register::re); }
std::string test_rf() { return tester(0xf123456789345678, Register::rf); }

// Cache Control Ranges
// 000: 64-bit
// 001: 8-bit
// 010: 16-bit
// 011: 24-bit
// 100: 32-bit
// 101: 40-bit
// 110: 48-bit
// 111: 56-bit

struct CacheControl
{
   uint8_t rtype  : 4{}; // determines which register we can load into
   uint8_t range  : 3{}; // size masks - see above
   uint8_t packed : 1{}; // indicates if we've packed yet
   uint8_t unused1{};
   uint8_t unused2{};
   uint8_t unused3{};
};
static_assert(sizeof(CacheControl) == 4, "Cache Control must be 32-bit on x86-64.");

uint64_t countLeadingZeros(const uint64_t value)
{
  uint64_t mask = 0x8000000000000000;
  uint64_t leading = 0;
  while (((mask & value) == 0) && mask != 0)
  {
    mask = mask >> 1;
    ++leading;
  }

  return leading;
}

CacheControl extractCacheControl(const CacheLine& c)
{
  CacheControl result;
  result.rtype = (c.b0 & 0xF) >> 60;
  uint64_t leading = countLeadingZeros(c.b0);
  uint64_t next = countLeadingZeros(c.b1);
  if (next < leading) { leading = next; }
  next = countLeadingZeros(c.b2);
  if (next < leading) { leading = next; }
  next = countLeadingZeros(c.b3);
  if (next < leading) { leading = next; }
  next = countLeadingZeros(c.b4);
  if (next < leading) { leading = next; }
  next = countLeadingZeros(c.b5);
  if (next < leading) { leading = next; }
  next = countLeadingZeros(c.b6);
  if (next < leading) { leading = next; }
  next = countLeadingZeros(c.b7);
  if (next < leading) { leading = next; }

  if (leading >=  8) { result.range = 0b111; }
  if (leading >= 16) { result.range = 0b110; }
  if (leading >= 24) { result.range = 0b101; }
  if (leading >= 32) { result.range = 0b100; }
  if (leading >= 40) { result.range = 0b011; }
  if (leading >= 48) { result.range = 0b010; }
  if (leading >= 56) { result.range = 0b001; }
  result.packed = 1;
  
  return result;
}

uint64_t extractBitLength(const CacheLine& c)
{
  CacheControl control = extractCacheControl(c);
  switch (control.range)
  {
    case 0b111:
      return 56;
    case 0b110:
      return 48;
    case 0b101:
      return 40;
    case 0b100:
      return 32;
    case 0b011:
      return 24;
    case 0b010:
      return 16;
    case 0b001:
      return 8;
    case 0:
    default:
      return 64;
  }
}

// Encode + Decode
// 1. Given a vector, we will re-encode it to optimize for 64K loads
// 2. The resulting multi-vector will be 16 parallel vectors, smaller in size
// 3. the first four bits of each parallel vector encode the lowest 4 bits of
//    each value - to help ensure that we actually balance the arrays.
// 4. Those bits are used to determine which register to load to - this is not
//    yet consistent with the code in this file (8/24/2025).
// 5. FastVector is normalized to store integers with as few bits as possible

template <typename T>
struct FastVector
{
  std::vector<T> r0;
  std::vector<T> r1;
  std::vector<T> r2;
  std::vector<T> r3;
  std::vector<T> r4;
  std::vector<T> r5;
  std::vector<T> r6;
  std::vector<T> r7;
  std::vector<T> r8;
  std::vector<T> r9;
  std::vector<T> ra;
  std::vector<T> rb;
  std::vector<T> rc;
  std::vector<T> rd;
  std::vector<T> re;
  std::vector<T> rf;
};
std::ostream& operator<<(std::ostream& o, const FastVector& fv)
{
  std::cout << static_cast<int>(fv.r0) << ", "
            << static_cast<int>(fv.r1) << ", "
            << static_cast<int>(fv.r2) << ", "
            << static_cast<int>(fv.r3) << ", "
            << static_cast<int>(fv.r4) << ", "
            << static_cast<int>(fv.r5) << ", "
            << static_cast<int>(fv.r6) << ", "
            << static_cast<int>(fv.r7) << ", "
            << static_cast<int>(fv.r8) << ", "
            << static_cast<int>(fv.r9) << ", "
            << static_cast<int>(fv.ra) << ", "
            << static_cast<int>(fv.rb) << ", "
            << static_cast<int>(fv.rc) << ", "
            << static_cast<int>(fv.rd) << ", "
            << static_cast<int>(fv.re) << ", "
            << static_cast<int>(fv.rf);
}

template <typename T>
FastVector<T> encode(const std::vector<T>& input)
{
  // stub
  FastVector<T> result;
  for (const T& ith: input)
  {
    switch (ith & 0xF)
    {
      case 15: result.rf.push_back(ith); break;
      case 14: result.re.push_back(ith); break;
      case 13: result.rd.push_back(ith); break;
      case 12: result.rc.push_back(ith); break;
      case 11: result.rb.push_back(ith); break;
      case 10: result.ra.push_back(ith); break;
      case 9: result.r9.push_back(ith); break;
      case 8: result.r8.push_back(ith); break;
      case 7: result.r7.push_back(ith); break;
      case 6: result.r6.push_back(ith); break;
      case 5: result.r5.push_back(ith); break;
      case 4: result.r4.push_back(ith); break;
      case 3: result.r3.push_back(ith); break;
      case 2: result.r2.push_back(ith); break;
      case 1: result.r1.push_back(ith); break;
      case 0: result.r0.push_back(ith); break;
      default: throw std::runtime_error("impossible error"); break;
    }
  }

  return result;
}

template <typename T>
std::vector<T> decode(const FastVector<T>& input)
{
  std::vector<T> result;
  for (const T& ith : input.r0) { result.push_back(ith); }
  for (const T& ith : input.r1) { result.push_back(ith); }
  for (const T& ith : input.r2) { result.push_back(ith); }
  for (const T& ith : input.r3) { result.push_back(ith); }
  for (const T& ith : input.r4) { result.push_back(ith); }
  for (const T& ith : input.r5) { result.push_back(ith); }
  for (const T& ith : input.r6) { result.push_back(ith); }
  for (const T& ith : input.r7) { result.push_back(ith); }
  for (const T& ith : input.r8) { result.push_back(ith); }
  for (const T& ith : input.r9) { result.push_back(ith); }
  for (const T& ith : input.ra) { result.push_back(ith); }
  for (const T& ith : input.rb) { result.push_back(ith); }
  for (const T& ith : input.rc) { result.push_back(ith); }
  for (const T& ith : input.rd) { result.push_back(ith); }
  for (const T& ith : input.re) { result.push_back(ith); }
  for (const T& ith : input.rf) { result.push_back(ith); }
  return result;
}

uint64_t extraBytesAvailable(const CacheLine& c)
{
  // Our extra 28 bits are pulled 4 bits at a time from each 64-bit value
  CacheControl control = extractCacheControl(c);
  std::cout << "CC.rtype=" << (int)control.rtype << ", CC.range=" << (int)control.range << std::endl;
  uint64_t containerSize = extractBitLength(c);
  std::cout << "Container Size = " << containerSize << std::endl;

  switch (containerSize)
  {
    case 64:
    default:
      return 3;
      break;
  }

  return 0;
}

std::string testLeadingZeros(const uint64_t value, const uint64_t expected)
{
  uint64_t test = countLeadingZeros(value);
  return (test == expected) ? "OK\n" : "Failed\n";
}

using namespace std;
int main()
{
  CacheLine test;

  bool verifyLeadingZeros = false;
  if (verifyLeadingZeros) {
  cout <<  "test0: " << testLeadingZeros(0xffffffffffffffff, 0);
  cout <<  "test4: " << testLeadingZeros(0x0fffffffffffffff, 4);
  cout <<  "test5: " << testLeadingZeros(0x07ffffffffffffff, 5);
  cout <<  "test6: " << testLeadingZeros(0x03ffffffffffffff, 6);
  cout <<  "test7: " << testLeadingZeros(0x01ffffffffffffff, 7);
  cout <<  "test8: " << testLeadingZeros(0x00ffffffffffffff, 8);
  cout << "test25: " << testLeadingZeros(0x0000007fffffffff, 25);
  cout << "test63: " << testLeadingZeros(0x0000000000000001, 63);
  cout << "test64: " << testLeadingZeros(0x0000000000000000, 64);
  }

  bool verifyRegisters = false;
  if (verifyRegisters)
  {
  cout << "r0: " << test_r0() << endl;
  cout << "r1: " << test_r1() << endl;
  cout << "r2: " << test_r2() << endl;
  cout << "r3: " << test_r3() << endl;
  cout << "r4: " << test_r4() << endl;
  cout << "r5: " << test_r5() << endl;
  cout << "r6: " << test_r6() << endl;
  cout << "r7: " << test_r7() << endl;
  cout << "r8: " << test_r8() << endl;
  cout << "r9: " << test_r9() << endl;
  cout << "ra: " << test_ra() << endl;
  cout << "rb: " << test_rb() << endl;
  cout << "rc: " << test_rc() << endl;
  cout << "rd: " << test_rd() << endl;
  cout << "re: " << test_re() << endl;
  cout << "rf: " << test_rf() << endl;
  }

  bool testExtraBytes = false;
  if (testExtraBytes) {
  uint64_t expansion = extraBytesAvailable(test);
  cout << "Expanded test by " << expansion << " bytes.\n";
  }

  std::vector<uint64_t> stuff { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 };
  FastVector<uint64_t> split = encode(stuff);
  cout << "FV.r0 = " << split.r0 << endl;
  cout << "FV.r1 = " << split.r1 << endl;
  cout << "FV.r2 = " << split.r2 << endl;
  cout << "FV.r3 = " << split.r3 << endl;
  cout << "FV.r4 = " << split.r4 << endl;
  cout << "FV.r5 = " << split.r5 << endl;
  cout << "FV.r6 = " << split.r6 << endl;
  cout << "FV.r7 = " << split.r7 << endl;
  cout << "FV.r8 = " << split.r8 << endl;
  cout << "FV.r9 = " << split.r9 << endl;
  cout << "FV.ra = " << split.ra << endl;
  cout << "FV.rb = " << split.rb << endl;
  cout << "FV.rc = " << split.rc << endl;
  cout << "FV.rd = " << split.rd << endl;
  cout << "FV.re = " << split.re << endl;
  cout << "FV.rf = " << split.rf << endl;
}
