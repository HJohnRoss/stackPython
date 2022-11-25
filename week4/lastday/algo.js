/* 
  String Anagrams
  Given a string,
  return array where each element is a string representing a different anagram (a different sequence of the letters in that string).
  Ok to use built in methods
*/

const str1 = "lim";
const expected1 = ["ilm", "iml", "lim", "lmi", "mil", "mli"];
// Order of the output array does not matter

/**
 * Add params if needed for recursion.
 * Generates all anagrams of the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {Array<string>} All anagrams of the given str.
 */
// You will need more parameters!
// var result_arr = []
// function generateAnagrams(str, arr = str.split(''), result_arr) {
//     if (arr = []) {
//         return arr
//     }
//     let temp = arr.pop()
//     let temp2 = temp
//     for (let i = 0; i < arr.length; i++) {
//         temp += arr[i]
//     }
//     result_arr.push(temp)
//     for (let x = arr.length - 1; x >= 0; x--) {
//         temp2 += arr[x]
//     }
//     result_arr.push(temp2)
//     console.log(temp2)
//     generateAnagrams(str, arr, result_arr)
// }
function generateAnagrams(str, partial="", anagrams=[]){
    if (str.length === 0) {
        anagrams.push(partial)
    } 
    for (let i = 0; i < str.length; i++) {
        const currectLetter = str[i]
        const beforeLetter = str.slice(0,i)
        const afterLetter = str.slice(i+1)
        const remainingStr = beforeLetter + afterLetter
        const newPartial = partial + currectLetter
        generateAnagrams(remainingStr, newPartial, anagrams)
    }
    return anagrams
}

console.log(generateAnagrams(str1)) //["ilm", "iml", "lim", "lmi", "mil", "mli"] (order may vary, that's okay)