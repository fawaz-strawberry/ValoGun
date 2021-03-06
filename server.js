const express = require('express');

const bodyParser = require('body-parser');
const { reset } = require('nodemon');
const robot = require('robotjs');


const app = express();
const port = 4000;

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}));

var forward = [0, 0, 0]
var up = [0, 0, 0]
var right = [0, 0, 0]


//direction 1 is forward, direction 2 is right, direciton 3 is up
var direction = 0

const finalAmount = 20
var averageAmount = 0

app.listen(port, () => {
  console.log(`Success! Your application is running on port ${port}.`);
});

app.get('/', (req, res) => {
    res.send('Homepage')
})

app.post("/sendData", (req, res) => {
  
  let date_obj = new Date()

  var d = new Date();
  var n = d.getMilliseconds();

  // console.log("Direction: " + direction + " AverageAmount: " + averageAmount)

  if(direction == 1 && averageAmount > 0)
  {
      forward[0] += req.body.x
      forward[1] += req.body.y
      forward[2] += req.body.z

      averageAmount -= 1

      if(averageAmount == 0)
      {
        forward[0] = forward[0] / finalAmount
        forward[1] = forward[1] / finalAmount
        forward[2] = forward[2] / finalAmount

        console.log(" ------------------------------------ ")
        console.log(forward)
        console.log(up)
        console.log(right)
        console.log(" ------------------------------------ ")

        res.send("Front Calibration Complete")
      }
      else
      {
        res.send("Calibrating Front")
      }

      
  }
  else if(direction == 2 && averageAmount > 0)
  {
      up[0] += req.body.x
      up[1] += req.body.y
      up[2] += req.body.z

      averageAmount -= 1

      if(averageAmount == 0)
      {
        up[0] = up[0] / finalAmount
        up[1] = up[1] / finalAmount
        up[2] = up[2] / finalAmount

        console.log(" ------------------------------------ ")
        console.log(forward)
        console.log(up)
        console.log(right)
        console.log(" ------------------------------------ ")

        res.send("Up Calibration Complete")
      
      }
      else
      {
        res.send("Calibrating Up")
      }
      
  }
  else if(direction == 3 && averageAmount > 0)
  {
      right[0] += req.body.x
      right[1] += req.body.y
      right[2] += req.body.z

      averageAmount -= 1

      if(averageAmount == 0)
      {
        right[0] = right[0] / finalAmount
        right[1] = right[1] / finalAmount
        right[2] = right[2] / finalAmount

        console.log(" ------------------------------------ ")
        console.log(forward)
        console.log(up)
        console.log(right)
        console.log(" ------------------------------------ ")

        res.send("Right Calibration Complete")
      }
      else
      {
        res.send("Calibrating Right")
      }

      

  }
  else
  {
    //console.log("Request Time: " + req.body.time + " ---- Response Time: " + n)
    res.send("Success")
  }
  
})

app.post("/startCalibration", (req, res) => {

    

    if(averageAmount <= 0)
    {
      direction = req.body.calibration
      averageAmount = finalAmount
  
      if(direction == 1)
      {
        forward = [0, 0, 0]
        res.send("Calibrating Front Please Aim Steady")
      }
      else if(direction == 2)
      {
        up = [0, 0, 0]
        res.send("Calibrating Up Please Aim Steady")
      }
      else if(direction == 3)
      {
        right = [0, 0, 0]

        res.send("Calibrating Right Please Aim Steady")
      }
      else
      {
        direction = 0
        averageAmount = 0
        res.send("Calibrating Complete")
        
      }
    }
    else
    {
      res.send("Waiting to finish current calibration")
    }

    
})

app.get("/ability0", (req, res) => {
  console.log("Activating Ability 0")
  robot.keyTap('c');
  res.send("Activated")
})

app.get("/ability1", (req, res) => {
  console.log("Activating Ability 1")
  robot.keyTap('q');
  res.send("Activated")
})

app.get("/ability2", (req, res) => {
  console.log("Activating Ability 2")
  robot.keyTap('e');
  res.send("Activated")
})

app.get("/ability3", (req, res) => {
  console.log("Activating Ability 3")
  res.send("Activated")
  robot.keyTap('x');
})

app.get("/runUp", (reqd, res) => {
  console.log("Running Up")
  res.send("Activated")
  robot.keyToggle('d', "down");
})

app.get("/runDown", (req, res) => {
  console.log("Running Down")
  res.send("Activated")
  robot.keyToggle('a', "down");
})

app.get("/runLeft", (req, res) => {
  console.log("Running Left")
  res.send("Activated")
  robot.keyToggle('w', "down");
})

app.get("/runRight", (req, res) => {
  console.log("Running Right")
  res.send("Activated")
  robot.keyToggle('s', "down");
})

app.get("/cancelHorizontalRun", (req, res) => {
  console.log("Cancelling Horizontal Run")
  res.send("Activated")
  robot.keyToggle("w", "up")
  robot.keyToggle("s", "up")
})

app.get("/cancelVerticalRun", (req, res) => {
  console.log("Cancelling Vertical Run")
  res.send("Activated")
  robot.keyToggle("a", "up")
  robot.keyToggle("d", "up")
})

app.get("/buyWeapon", (req, res) => {
  console.log("Buying Weapon")
  res.send("Buying Weapon Success")
  robot.keyTap("b")
})

app.get("/closeWeapon", (req, res) => {
  console.log("Buying Weapon")
  res.send("Buying Weapon Success")
  robot.keyToggle("b", "up")
})


var weapon_num = 1
app.get("/swapWeapon", (req, res) => {
  console.log("Switching to weapon")
  res.send("Switching to weapon " + weapon_num)
  robot.keyToggle("" + weapon_num, "down")

})

app.get("/stopWeapon", (req, res) => {
  console.log("Switching to weapon")
  res.send("Switching to weapon " + weapon_num)
  robot.keyToggle("" + weapon_num, "up")
  weapon_num += 1
  if (weapon_num === 5)
  {
    weapon_num = 1
  }

})

app.get("/jump", (req, res) => {
  console.log("Jumping")
  res.send("Jumping!")
  robot.keyTap("space")
})

app.get("/crouch", (req, res) => {
  console.log("Crouching")
  res.send("Crouching!")
  robot.keyToggle("shift", "down")
})

app.get("/stand", (req, res) => {
  console.log("Crouching")
  res.send("Crouching!")
  robot.keyToggle("shift", "up")
})