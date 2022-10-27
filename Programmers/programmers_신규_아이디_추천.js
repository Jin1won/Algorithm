function solution(new_id) {
  let answer = new_id
    .toLowerCase()
    .replace(/[^a-z\d-_.]/g, "")
    .replace(/\.{2,}/g, ".")
    .replace(/^\./, "")
    .replace(/^$/, "a")
    .slice(0, 15)
    .replace(/\.$/, "");

  return answer.length <= 2
    ? (answer = answer.padEnd(3, answer[answer.length - 1]))
    : answer;
}
