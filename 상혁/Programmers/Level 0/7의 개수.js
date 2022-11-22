function solution(array) {
  const list = array.join('').split('');

  return list.filter((v) => v === '7').length;
}
