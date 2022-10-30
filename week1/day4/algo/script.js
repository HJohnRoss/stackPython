const str1 = "aaaabbcdddaaa";
const expected1 = "a4b2cd3a3";
const expected1b = "a4bbcd3a3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "ccbb";
const expected4 = "ccbb";

const str5 = "abbbbbbbbbbbbbbbbb"
const expected5 = "ab17"



function encodeStr(str) {
  var newStr = ""
  var counter = 1
  for (var i = 0; i < str.length; i++) {
    if (str[i] == str[i + 1]) {
      counter++
    } else {
      if (counter <= 1) {
        newStr += str[i]
      } else {
        newStr += (str[i] + counter)
      }
      counter = 1
    }
  }
  if (newStr.length >= str.length) {
    return str
  }
  return newStr
}

console.log(encodeStr(str1)) // Expected: a4bbcd3
console.log(encodeStr(str2)) // Expected: ""
console.log(encodeStr(str3)) // Expected: a
console.log(encodeStr(str4)) // Expected: bbcc
console.log(encodeStr(str5)) // Expected: ab17

const strA = "a3b2c1d3";
const expectedA = "aaabbcddd";

const strB = "a3b2c12d10";
const expectedB = "aaabbccccccccccccdddddddddd";


//helpful built-ins : isNaN() .repeat() parseInt() NaN
function decodeStr(str) {
  var newStr = ""
  for (var i = 0; i < str.length; i++) {
    if (isNaN(str[i]) == true) {
      newStr += str[i - 1]
    }
    return newStr
  }
}

console.log(decodeStr(strA)) // Expected: aaabbcddd
console.log(decodeStr(strB)) // Expected: aaabbccccccccccccdddddddddd