console.log("Print all numbers between -10 and 19");
var num=-10;
while (num<=19)
{
	console.log(num);
	num++;
}
console.log("Print all even numbers between 10 and 40");
var num=10;
while (num<=40)
{
	console.log(num);
	num+=2;
}
console.log("Print all odd numbers between 300 and 333");
var num=300;
while (num<=333)
{
	if (num%2!==0) {


	console.log(num);
	
}
num++;
}
console.log("Print all numbers divisible by 5 AND 3 between 5 and 50");
var num=5;
while (num<=50)
{
	if (num%5===0&&num%3===0) {


	console.log(num);
	
}
num++;
}
console.log("Method 1");
var str=prompt("Are you there yet!");
while(str!=="yes"&&str!=="yeah"){
var str=prompt("Are you there yet!");
}
if (str==="yes"||str==="yeah") {
	alert("yay,you made it");
}
 
console.log("Method 2");
var str=prompt("Are you there yet?");
while(str.indexOf("yes")=== -1&&str.indexOf("yeah")=== -1)
{
var str=prompt("Are you there yet!");
}

	alert("yay,you made it");