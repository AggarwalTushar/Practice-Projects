import './App.css';
import { useState } from 'react';
import Button from './components/Button';
import BlogContent from './components/blogContent';
const origblogs=[
  {user:'Roger Federer',heading:'Something About Roger Federer',description:'Roger Federer is a Swiss professional tennis player. He is ranked No. 8 in the world by the Association of Tennis Professionals.He has won 20 Grand Slam mens singles titles, an all-time record shared with Rafael Nadal...'},
  {user:'Roger Federer',heading:'Something About Roger Federer',description:'Roger Federer is a Swiss professional tennis player. He is ranked No. 8 in the world by the Association of Tennis Professionals.He has won 20 Grand Slam mens singles titles, an all-time record shared with Rafael Nadal...'},
  {user:'Roger Federer',heading:'Something About Roger Federer',description:'Roger Federer is a Swiss professional tennis player. He is ranked No. 8 in the world by the Association of Tennis Professionals.He has won 20 Grand Slam mens singles titles, an all-time record shared with Rafael Nadal...'},
  {user:'Roger Federer',heading:'Something About Roger Federer',description:'Roger Federer is a Swiss professional tennis player. He is ranked No. 8 in the world by the Association of Tennis Professionals.He has won 20 Grand Slam mens singles titles, an all-time record shared with Rafael Nadal...'},
  {user:'Roger Federer',heading:'Something About Roger Federer',description:'Roger Federer is a Swiss professional tennis player. He is ranked No. 8 in the world by the Association of Tennis Professionals.He has won 20 Grand Slam mens singles titles, an all-time record shared with Rafael Nadal...'},
  {user:'Roger Federer',heading:'Something About Roger Federer',description:'Roger Federer is a Swiss professional tennis player. He is ranked No. 8 in the world by the Association of Tennis Professionals.He has won 20 Grand Slam mens singles titles, an all-time record shared with Rafael Nadal...'}

];
function App() {
  const [blogs,setBlogs]=useState(origblogs);
  const [hide,setHide]=useState(false);
  const addBlog=blog=>{
      setBlogs(prev=>[...prev,blog]);
  }
  const deleteBlog=index=>{
    setBlogs(state=>state.filter((blog,ind)=>ind!==index));
  }
  const hideHandler=()=>{
    setHide(prev=>!prev);
  }
  return (
    <div className="bg pb-4">
      <div className="container-fluid">
          <div className="row">
              <div className="col-8">
                  <img src="https://iitgoa.ac.in/img/iit-goa-logo.svg" alt='Some Error' className="iitgoa-logo" id="iitgoa-logo" />
                  <img src="https://iic-iitgoa.herokuapp.com/static/media/iiclogo.8c5058e9.svg" alt='Some Error' className="iic-logo" id="iic-logo" />
              </div>
              <div className="col-4">
                <img src="https://iic-iitgoa.herokuapp.com/static/media/menu.a3357bf5.svg" alt='Some Error' className="ml-auto mr-2" id="nav-img" style={{cursor: 'pointer',width:'50px'}} />
              </div>
          </div>
      </div>
      <div className={hide?'container-fluid':'container'}>
        <div className="row">
          <div className="col-12 text-center mb-3">
            <h1 className="heading" id="heading1">BLOGS PAGE</h1>
          </div>
          <BlogContent hide={hideHandler} delete={deleteBlog} blogs={blogs}/>
          {!hide&&<div className='col-12'>
            <div className='d-flex justify-content-end'>
              <Button addBlog={addBlog}/>
            </div>
          </div>}
        </div>
      </div>
    </div>
   
  );
}

export default App;
