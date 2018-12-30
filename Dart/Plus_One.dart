plusOne(List<int> digits) {
  for(int i = digits.length - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      ++digits[i];
      return digits;
    } 
    digits[i] = 0;
  }
  return [1] + digits;
}

void main() {
  print(plusOne([1, 2, 3]));
  print(plusOne([9, 9, 9]));
  print(plusOne([0]));
}