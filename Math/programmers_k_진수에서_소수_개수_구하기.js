function solution(n, k) {
  let answer = 0;

  const kValue_list = getKValue(n, k).split("0");

  kValue_list.forEach((value) => {
    if (value !== "") {
      if (isPrimeNumber(value)) {
        answer += 1;
      }
    }
  });

  return answer;
}

function getKValue(num, k) {
  let n = num;
  let kValue = "";
  while (n > 0) {
    kValue += n % k;
    n = Math.floor(n / k);
  }
  return kValue.split("").reverse().join("");
}

function isPrimeNumber(num) {
  if (num <= 1) {
    return false;
  }

  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }

  return true;
}
