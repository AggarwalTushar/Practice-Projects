import { trim } from 'jquery';
import React, { useState } from 'react';
import { useRef } from 'react';
import './Button.module.css';
const Button=props=>{
    const titleInputRef=useRef();
    const nameInputRef=useRef();
    const descInputRef=useRef();
    const [error,setError]=useState(false);
    const save=()=>{
        const title=titleInputRef.current.value;
        const name=nameInputRef.current.value;
        const desc=descInputRef.current.value;
        if(title.trim().length===0||name.trim().length===0||desc.trim().length===0){
            setError(true);
            return;
        }
        props.addBlog({heading:title,user:name,description:desc});
        setError(false);
        titleInputRef.current.value='';
        nameInputRef.current.value='';
        descInputRef.current.value='';
    }
    const closeHandler=()=>setError(false);
    return(
        <React.Fragment>
            <button type="button" className="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                Add A New Blog
              </button>
              <div className="modal fade modal-fullscreen" id="exampleModal" tabIndex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div className="modal-dialog">
                  <div className="modal-content">
                    <div className="modal-header">
                      <h5 className="modal-title" id="exampleModalLabel">Enter Blog Details</h5>
                      <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div className="modal-body">
                        <div className='d-flex flex-column'>
                            <label htmlFor='name'>Name</label>
                            <input ref={nameInputRef} id='name' type='text' placeholder='Enter Your Name'/>
                            <label htmlFor='heading'>Blog-Title</label>
                            <input ref={titleInputRef} id='heading' placeholder='Enter a suitable heading' type='text'/>
                            <label htmlFor='description'>Description</label>
                            <textarea ref={descInputRef} id='description' placeholder='Share something'></textarea>
                        </div>
                        {error&&<p style={{color:'red'}}>Fields cannot be empty!</p>}
                    </div>
                    <div className="modal-footer">
                      <button type="button" className="btn btn-secondary" onClick={closeHandler} data-bs-dismiss="modal">Close</button>
                      <button type="button" className="btn btn-primary" onClick={save}>Add Blog</button>
                    </div>
                  </div>
                </div>
              </div>
        </React.Fragment>
    )
}
export default Button;