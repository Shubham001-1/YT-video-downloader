import express from "express" ;
import axios from 'axios';
import cors from "cors"
const app = express() ;
app.use(express.json());
app.use(cors(
    {origin : "*" } 
));


const port = 8000 ;
const downloadVideo = async (urldoc,qualitydoc,formatdoc) => {
  try {
    const response = await axios.post('http://localhost:5001/download', {
      urldoc,
      qualitydoc,
      formatdoc
    }, {
    headers: {
      'Content-Type': 'application/json'  
    }
  });

    console.log( response.data);
  } catch (error) {
    
    console.error( error.response?.data || error.message);
  }
};

app.post('/downloadvideo',async (req,res)=>{
    const{ urldoc,qualitydoc,formatdoc }= req.body ;
    await downloadVideo(urldoc,qualitydoc,formatdoc) ;
     return res.status(200).send('downloaded succesfully download it from'); 
    });


app.listen(port,()=>{
    console.log("server is running ")
})
