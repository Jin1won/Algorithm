function solution(s) {
  let answer = [];
  let sList = s.slice(2, s.length - 2).split("},{");
  sList.sort((a, b) => a.length - b.length);

  sList.forEach((s) => {
    if (answer.length === 0) {
      answer.push(Number(s));
      return;
    }

    s.split(",")
      .map((ele) => Number(ele))
      .forEach((ele) => {
        if (!answer.includes(ele)) {
          answer.push(Number(ele));
          return;
        }
      });
  });

  return answer;
}
