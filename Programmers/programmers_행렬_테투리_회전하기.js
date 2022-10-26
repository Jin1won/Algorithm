function solution(rows, columns, queries) {
    let answer = [];
    let graph = Array.from(new Array(rows+1),()=>new Array(columns+1));
    for (let i = 1; i <= rows; i++) {
        for (let j = 1; j <= columns; j++) {
            graph[i][j] = (i - 1) * columns + j;
        }
    }
    
    for (let q = 0; q < queries.length; q++) {
        const [x1, y1, x2, y2] = queries[q];
        const stack = [];

        for (let i = y1; i < y2; i++) stack.push(graph[x1][i]);
        for (let i = x1; i < x2; i++) stack.push(graph[i][y2]);
        for (let i = y2; i > y1; i--) stack.push(graph[x2][i]);
        for (let i = x2; i > x1; i--) stack.push(graph[i][y1]);

        answer.push(Math.min(...stack));
        const temp = stack.pop();
        stack.unshift(temp);

        for (let i = y1; i < y2; i++) graph[x1][i] = stack.shift();
        for (let i = x1; i < x2; i++) graph[i][y2] = stack.shift();
        for (let i = y2; i > y1; i--) graph[x2][i] = stack.shift();
        for (let i = x2; i > x1; i--) graph[i][y1] = stack.shift();
  } 