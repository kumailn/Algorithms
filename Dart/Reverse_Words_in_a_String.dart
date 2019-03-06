//Question: Given a string, reverse the positions of the words, for example 'hi my name is' becomes 'is name my hi'
//Solution: Reverse string, then reverse each word
//Time Complexity: O(n)

String reverseWords(String strin) {
  List<String> reverse(int start, int end, List<String> str){
    while (start < end) {
      String temp = str[start];
      str[start] = str[end];
      str[end] = temp;

      start++;
      end--;
    } 
    return str;
  }

  List<String> new_strin = strin.split("").reversed.toList();

  int i = 0;
  while (i < new_strin.length) {
    int end = i;
    if (new_strin[i] != " ") {
      while (end + 1 < new_strin.length && new_strin[end] != " "){
        if (new_strin[end + 1] == " ") break;
        end++;
      }
    }
    new_strin = reverse(i, end, new_strin);
    i = end + 1;
  }

  return new_strin.join("");
}

main(List<String> args) {
  print(reverseWords("my name is"));
}