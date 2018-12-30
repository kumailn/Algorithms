String firstUniqChar(String str) {
  Map letterCounts = Map();
  for(int i=0; i<str.length; i++){
    if (letterCounts.containsKey(str[i])) letterCounts[str[i]]++;
    else letterCounts[str[i]] = 1;
  }

  for(int i=0; i<str.length; i++){
    if(letterCounts[str[i]] == 1) return str[i];
  }

  return "";
}

void main() {
  print(firstUniqChar('kayak'));
}