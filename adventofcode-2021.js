https://adventofcode.com/2021

// day 1 - part 1
let prev=null;
let total=0;
for(let a=0; a<input.length; a+=1) {
    i=input[a];
    if (prev!=null && prev<i) {total += 1;}
    prev=i;
}
console.log(total)
// 1688

// day 1 - part 2
let tmp=[input[0],input[1],input[2]];
let total=0;
for(let a=3; a<input.length; a+=1) {
    prev = tmp[0] + tmp[1] + tmp[2];

    i=input[a];
    cur = tmp[1] + tmp[2] + i
    if (cur > prev) {total += 1;}

    tmp[0] = tmp[1]
    tmp[1] = tmp[2]
    tmp[2] = i
}
console.log(total)
// 1728

// day 2 - part 1
let x=0;
let y=0;
for(let a=0; a<input.length;a+=1) {
    let i = input[a];
    if (i[0] === 'forward') x += i[1];
    else if (i[0] === 'up') y -= i[1];
    else if (i[0] === 'down') y += i[1];
}
console.log(x*y);
// 1660158

// day 2 - part 2
let x=0;
let y=0;
let aim=0;
for(let a=0; a<input.length;a+=1) {
    let i = input[a];
    if (i[0] === 'forward') {x += i[1]; y += (aim * i[1]); }
    else if (i[0] === 'up') aim -= i[1];
    else if (i[0] === 'down') aim += i[1];
}
console.log(x*y);
// 1604592846

// day 3 - part 1
