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

template <typename T>
std::ostream& operator<<(std::ostream& o, const FastVector<T>& fv)
{
  using namespace std;
  o<<"r0: ";for(const T& ith : fv.r0){o<< static_cast<int>(ith) << " "; }; o << endl;
  o<<"r1: ";for(const T& jth : fv.r1){o<< static_cast<int>(jth) << " "; }; o << endl;
  o<<"r2: ";for(const T& kth : fv.r2){o<< static_cast<int>(kth) << " "; }; o << endl;
  o<<"r3: ";for(const T& lth : fv.r3){o<< static_cast<int>(lth) << " "; }; o << endl;
  o<<"r4: ";for(const T& mth : fv.r4){o<< static_cast<int>(mth) << " "; }; o << endl;
  o<<"r5: ";for(const T& nth : fv.r5){o<< static_cast<int>(nth) << " "; }; o << endl;
  o<<"r6: ";for(const T& oth : fv.r6){o<< static_cast<int>(oth) << " "; }; o << endl;
  o<<"r7: ";for(const T& pth : fv.r7){o<< static_cast<int>(pth) << " "; }; o << endl;
  o<<"r8: ";for(const T& qth : fv.r8){o<< static_cast<int>(qth) << " "; }; o << endl;
  o<<"r9: ";for(const T& rth : fv.r9){o<< static_cast<int>(rth) << " "; }; o << endl;
  o<<"ra: ";for(const T& sth : fv.ra){o<< static_cast<int>(sth) << " "; }; o << endl;
  o<<"rb: ";for(const T& tth : fv.rb){o<< static_cast<int>(tth) << " "; }; o << endl;
  o<<"rc: ";for(const T& uth : fv.rc){o<< static_cast<int>(uth) << " "; }; o << endl;
  o<<"rd: ";for(const T& vth : fv.rd){o<< static_cast<int>(vth) << " "; }; o << endl;
  o<<"re: ";for(const T& wth : fv.re){o<< static_cast<int>(wth) << " "; }; o << endl;
  o<<"rf: ";for(const T& xth : fv.rf){o<< static_cast<int>(xth) << " "; }; o << endl;
  return o;
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
  size_t ith{}; size_t jth{}; size_t kth{}; size_t lth{};
  size_t mth{}; size_t nth{}; size_t oth{}; size_t pth{};
  size_t qth{}; size_t rth{}; size_t sth{}; size_t tth{};
  size_t uth{}; size_t vth{}; size_t wth{}; size_t xth{};
  bool done = false;
  //while (!done)
  {
    // TODO: iterate in natural order so we can decode properly
  }
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

  vector<uint64_t> stuff { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40 };
  FastVector<uint64_t> split = encode(stuff);
  vector<uint64_t> r1 = decode(split);
  cout << "Fast Vector Test 1: " << split << endl;
  cout << "Test 1: " << ((stuff == r1) ? "OK" : "Failed") << endl;

  using fvi = FastVector<int>;
  using vi = vector<int>;
  vi test2data { 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21 };
  fvi test2 = encode(test2data);
  vi r2 = decode(test2);
  cout << "Fast Vector Test 2: " << test2 << endl;
  cout << "Test 2: " << ((test2data == r2) ? "OK" : "Failed") << endl;
}
