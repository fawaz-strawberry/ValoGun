const express = require('express');

const bodyParser = require('body-parser')


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