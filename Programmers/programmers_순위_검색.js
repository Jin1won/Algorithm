function solution(info, query) {
  const answer = [];

  const participants = {};

  info.forEach((inf, idx) => {
    let informations = inf.split(" ");
    let score = informations.pop();

    possibilities(informations, score, participants, 0);
  });

  for (const key in participants) {
    participants[key] = participants[key].sort((a, b) => a - b);
  }

  query.forEach((q) => {
    let queryInfo = q.split(" ").filter((item) => item !== "and");
    let score = queryInfo.pop();
    queryInfo = queryInfo.join("");

    if (participants[queryInfo]) {
      answer.push(
        participants[queryInfo].length -
          binarySearch(score, participants[queryInfo])
      );
    } else {
      answer.push(0);
    }
  });

  return answer;
}

function possibilities(infos, score, map, start) {
  let key = infos.join("");
  let value = map[key];

  if (value) {
    map[key].push(+score);
  } else {
    map[key] = [+score];
  }

  for (let i = start; i < infos.length; i++) {
    let arr = [...infos];
    arr[i] = "-";
    possibilities(arr, score, map, i + 1);
  }
}

function binarySearch(score, arr) {
  let start = 0;
  let end = arr.length - 1;
  let mid = Math.floor((start + end) / 2);

  while (start <= end) {
    if (arr[mid] === score) return mid;

    if (arr[mid] < score) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }

    mid = Math.floor((start + end) / 2);
  }
  return mid + 1;
}
