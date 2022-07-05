//For-in loop
var friends = ['Kirtan','Aman','Kavish']
for(let friend in friends ){
  console.log(friend)
}
//output
//0
//1
//2

//for-of loop
for(let friend of friends){
  console.log(friend)
}
//output
//Kirtan
//Aman
//Kavish
//use of forEach


friends.forEach(function(element,index,array){
  console.log(`${element} ${index} ${array}`)
})

friends.forEach((element,index,array) => {
  console.log(`${element} ${index} ${array}`)
})
