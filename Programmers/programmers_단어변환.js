function solution(begin, target, words) {
  let answer = 0;
  let visited = new Array(words.length).fill(false);
  let queue = [];

  if (!words.includes(target)) return 0;

  function bfs(word, cnt) {
    queue.push([word, cnt]);
    while (queue.length) {
      let [currentWord, cnt] = queue.shift();

      if (currentWord == target) return cnt;

      words.forEach((word, idx) => {
        let notEqual = 0;
        if (visited[idx]) return;

        for (let i = 0; i < word.length; i++) {
          if (word[i] !== currentWord[i]) notEqual += 1;
        }
        if (notEqual === 1) {
          queue.push([word, cnt + 1]);
          visited[idx] = true;
        }
      });
    }
  }

  answer = bfs(begin, 0);

  return answer;
}
