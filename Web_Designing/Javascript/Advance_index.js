//three variable declaration
//var => Function scope
// let and const => Block scope
function biodata(){
  //var
  var myFirstName = "Kavish"
  console.log(myFirstName)

  if(true){
    var myLastName= "Dhirawat"
    console.log("inner " + myFirstName);
    console.log("inner " + myLastName);
  }
  console.log('outer ' + myLastName);
}
biodata()
//let
function biodata(){
  let myFirstName = "Kavish"
  console.log(myFirstName)

  if(true){
   let myLastName= "Dhirawat"
    console.log("inner " + myFirstName);
    console.log("inner " + myLastName);
  }
  //shows error, lifeline lasts for brackets(block scope)
  console.log('outer ' + myLastName);
}
biodata()
//const
function biodata(){
  const myFirstName = "Kavish"
  console.log(myFirstName)

  if(true){
   const myLastName= "Dhirawat"
    console.log("inner " + myFirstName);
    console.log("inner " + myLastName);
  }
  //shows error, lifeline lasts for brackets(block scope)
  //Its value always be the same
  console.log('outer ' + myLastName);
}
biodata()
