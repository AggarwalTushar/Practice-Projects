import React from 'react';
import styles from './blogContent.module.css';
import { useState } from 'react';
function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;

    return [year, month, day].join('-');
}
const BlogContent=props=>{
    const [showDetails,setShowDetails]=useState(false);
    const detailsHandler=()=>{
        setShowDetails(prev=>!prev);
        props.hide();
    }
    return(
        <React.Fragment>
            {props.blogs.length==0 && <div className='col-12 text-center'><div className={`${styles['blog-card1']} d-flex flex-column justify-content-center`}><h2>No Blogs to show</h2></div></div>}
            {!showDetails&&props.blogs.map((blog,index)=>{
                return(<div key={index} className="col-12 col-md-4 mb-3">
                    <div className={`${styles['card']} shadow text-center`}>
                        <h1 className={styles['heading']}>{blog.heading}</h1>
                        <p style={{textAlign:'left'}}>{formatDate(new Date())}</p>
                        <p style={{textAlign:'left'}}>Posted By: {blog.user}</p>
                        <div>
                            <hr />
                            <p>{blog.description} <a href='#' onClick={detailsHandler}>Read More</a></p>
                            <hr />
                        </div>
                        <div className="d-flex flex-column">
                            <div style={{alignSelf:'flex-start'}}>
                                <span className={`fa fa-star ${styles.checked}`}></span>
                                <span className={`fa fa-star ${styles.checked}`}></span>
                                <span className={`fa fa-star ${styles.checked}`}></span>
                                <span className="fa fa-star"></span>
                                <span className="fa fa-star"></span>
                            </div>
                            <button style={{alignSelf:'flex-end'}} className="btn btn-danger" onClick={props.delete.bind(null,index)}>DELETE</button>
                        </div>
                    </div>
                </div>
            )})}
            {showDetails&&<React.Fragment> <div className='col-12 col-md-8 mb-3'>
            <img alt='Some Error' src='https://www.atptour.com/-/media/images/news/2021/06/16/18/45/federer-halle-2021-r2-reaction.jpg' className='w-100'/>
                    <div className={`${styles['card1']} shadow text-center`}>
                        <h1 className={styles['heading']}>Something About Roger Federer</h1>
                        <p style={{textAlign:'left'}}>{formatDate(new Date())}</p>
                        <p style={{textAlign:'left'}}>Posted By: Roger Federer</p>
                        <div>
                            <hr />
                            <p>Roger Federer (born 8 August 1981) is a Swiss professional tennis player. He is ranked No. 8 in the world by the Association of Tennis Professionals (ATP). He has won 20 Grand Slam men's singles titles, an all-time record shared with Rafael Nadal. Federer has been world No. 1 in the ATP rankings a total of 310 weeks – including a record 237 consecutive weeks – and has finished as the year-end No. 1 five times. Federer has won 103 ATP singles titles, the second-most of all-time behind Jimmy Connors and including a record six ATP Finals.

Federer has played in an era where he dominated men's tennis together with Rafael Nadal and Novak Djokovic, who have been collectively referred to as the Big Three and are widely considered three of the greatest tennis players of all-time.[c] A Wimbledon junior champion in 1998, Federer won his first Grand Slam singles title at Wimbledon in 2003 at age 21. In 2004, he won three out of the four major singles titles and the ATP Finals,[d] a feat he repeated in 2006 and 2007. From 2005 to 2010, Federer made 18 out of 19 major singles finals. During this span, he won his fifth consecutive titles at both Wimbledon and the US Open. He completed the career Grand Slam at the 2009 French Open after three previous runner-ups to Nadal, his main rival up until 2010. At age 27, he also surpassed Pete Sampras's then-record of 14 Grand Slam men's singles titles at Wimbledon in 2009.

Although Federer remained in the top 3 through most of the 2010s, the success of Djokovic and Nadal in particular ended his dominance over grass and hard courts. From mid-2010 through the end of 2016, he only won one major title. During this period, Federer and Stan Wawrinka led the Switzerland Davis Cup team to their first title in 2014, adding to the gold medal they won together in doubles at the 2008 Beijing Olympics. Federer also has a silver medal in singles from the 2012 London Olympics, where he finished runner-up to Andy Murray. After taking half a year off in late 2016 to recover from knee surgery, Federer had a renaissance at the majors. He won three more Grand Slam singles titles over the next two years, including the 2017 Australian Open over Nadal and a men's singles record eighth Wimbledon title later in 2017. He also became the oldest ATP world No. 1 in 2018 at age 36.</p>
                            <hr />
                        </div>
                        <div style={{textAlign:'left'}}>
                            <a className={`m-3 ${styles.link}`} href='#'>Like</a>
                            <a className={`m-2 ${styles.link}`} href='#'>Comment</a>
                        </div>
                        <div className="d-flex flex-row justify-content-end">
                            <div>
                                <span className={`fa fa-star ${styles.checked}`}></span>
                                <span className={`fa fa-star ${styles.checked}`}></span>
                                <span className={`fa fa-star ${styles.checked}`}></span>
                                <span className="fa fa-star"></span>
                                <span className="fa fa-star"></span>
                            </div>
                        </div>
                    </div>
                    <button type="button" onClick={detailsHandler} className="btn btn-primary mt-3">Back</button>
            </div>
            <div className={`col-3 d-none d-md-block row ${styles['recent']}`}>
                <div className='col-12'><h2>Recent Blogs</h2></div>
            {props.blogs.filter((blog,ind)=>ind<5).map((blog,index)=>{
                return(<div key={index} className="col-12 mb-4">
                    <div className={`${styles['card2']} shadow text-center`}>
                        <h1 className={styles['heading-small']}>{blog.heading}</h1>
                        <div>
                            <hr />
                            <p><a href='#' onClick={detailsHandler}>Read This Blog</a></p>
                            <hr />
                        </div>
                        <div className="d-flex flex-column">
                            <div style={{alignSelf:'flex-start'}}>
                                <span className={`fa fa-star ${styles.checked}`}></span>
                                <span className={`fa fa-star ${styles.checked}`}></span>
                                <span className={`fa fa-star ${styles.checked}`}></span>
                                <span className="fa fa-star"></span>
                                <span className="fa fa-star"></span>
                            </div>
                        </div>
                    </div>
                </div>
            )})}
            </div>
            </React.Fragment>
                }
        </React.Fragment>
    )
}
export default BlogContent;