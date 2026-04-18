import React from "react";


function Image({images, image, id, setImages}){

   

    function handleDelete(id){
    
        fetch(`/images/${id}`,{
            method:"DELETE"
        })
        .then(()=> {
            const filteredImages = images.filter(image =>{
            
            return (image.id !== id)
        })
        setImages(filteredImages)
    
        })
    
        
    }    
    if('Admin')
    return(
        
        <div className = 'image-card'>
            <img className = 'image-img' src = {image} alt = {id}/>
            <button className="delete_image" onClick={() => handleDelete(id)}>Delete</button>
        </div>
       
    );
    else
    return(
        <div className = 'image-card'>
            <img className = 'image-img' src = {image} alt = {id}/>
        </div>
       
        ) 
}
export default Image