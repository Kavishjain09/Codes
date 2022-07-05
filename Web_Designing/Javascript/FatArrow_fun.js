//normal Methods
console.log(sum())

function sum()
{
  let a=2, b=3;
  let sum = a+b;
  return `the sum of ${a},${b} is ${sum}`
}
//Or
console.log(mult())

function mult()
{
  let a=2, b=3;
  return `the multiply of ${a},${b} is ${a*b}`
}
//Fat-Arrow Method
const add = () =>
{
  let a=5, b=10;
 return `the addition of two no. is ${a+b}`
}
console.log(add());
//or
let a=5,b=10
const multi = () =>`the multiplication of two no. is ${a*b}`
console.log(multi());
