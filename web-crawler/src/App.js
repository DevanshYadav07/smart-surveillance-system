
import './App.css';
import React from 'react';
//import { useState } from 'react';
function App() {
  //const [data,setData]=useState(null);

  const handleSubmit=(e)=>{
    e.preventDefault();
    const first=e.target.fname.value;
    console.log(first);

  }
  return (
    <>
      <div className='container'>
        <form onSubmit={handleSubmit}> 
          <div className="row">
            <input type="text" name='fname' placeholder='websitelink'></input><br></br>
          </div>
          <div className='row'>
            <button className="btn btn-primary"> SUBMIT</button>
          </div>
        </form>
      </div>
    </>
  );
}

export default App;
