// 제재 아이디 후보로 가능한지 확인하는 함수
const isPossible = (uId, bId) => {
  // 1. 문자열 길이 비교
  if (uId.length !== bId.length) return false;
  // 2. 값이 '*'이 아닌 자리의 문자가 모두 같은지 확인
  let cnt = 0;
  for (let i = 0; i < uId.length; i++) {
    if (bId[i] !== "*" && uId[i] !== bId[i]) return false;
  }
  return true;
};
function solution(user_id, banned_id) {
  const visited = Array.from({ length: user_id.length }, () => false);
  const set = new Set();

  const DFS = (idx, cnt, possible) => {
    if (cnt === banned_id.length) {
      let arr = possible.split(" ");
      arr.shift(); // 맨 앞에 저장된 '' 값 제거
      arr.sort();
      let newStr = arr.join("");
      set.add(newStr);
    }
    if (idx >= user_id.length) return;

    for (let i = idx; i < banned_id.length; i++) {
      for (let j = 0; j < user_id.length; j++) {
        if (visited[j]) continue;
        if (!isPossible(user_id[j], banned_id[i])) continue;
        visited[j] = true;
        DFS(i + 1, cnt + 1, possible + " " + user_id[j]);
        visited[j] = false;
      }
    }
  };
  DFS(0, 0, "");

  return set.size;
}
