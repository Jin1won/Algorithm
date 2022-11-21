function solution(clothes) {
  let answer = 1;
  let ootd = {};

  for (cloth of clothes) {
    if (Object.keys(ootd).includes(cloth[1])) {
      ootd[cloth[1]] += 1;
    } else {
      ootd[cloth[1]] = 1;
    }
  }

  for (key of Object.keys(ootd)) {
    answer *= ootd[key] + 1;
  }

  return answer - 1;
}
