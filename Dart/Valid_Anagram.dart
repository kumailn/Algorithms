
bool isAnagram(String a, String b) {
  Map counts = new Map();

  for(int i = 0; i < a.length; i++) {
    if (counts.containsKey(a[i])) counts[a[i]] += 1;
    else counts[a[i]] = 1;

    if (counts.containsKey(b[i])) counts[b[i]] -= 1;
  }

  return counts.isEmpty;
}

main(List<String> args) {
  print(isAnagram('abcd', 'abdc'));
}