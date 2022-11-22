function solution(n, times) {
  let answer = 0;
  let [start, end] = [0, Math.max(...times) * n];
  let mid = 0;

  while (start <= end) {
    mid = Math.floor((start + end) / 2);
    let people = 0;
    times.forEach((time) => {
      people += Math.floor(mid / time);
    });
    if (people >= n) {
      end = mid - 1;
      answer = mid;
    } else {
      start = mid + 1;
    }
  }
  return answer;
}
