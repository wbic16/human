#include <iosfwd>
#include <iostream>
#include <string>

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

using namespace std;
int main()
{
	CacheLine test;
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
