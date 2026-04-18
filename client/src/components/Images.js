import React from "react";
import Image from "./Image";
import { useHistory, useParams } from "react-router-dom/cjs/react-router-dom.min";

function Images({images, setImages}){
    const {id} = useParams()
console.log(images)
    const history = useHistory()

    const handleClick =() => {
        history.push(`/newimage`)
    }
    const propertyImages = images.filter(image => image.property_id === parseInt(id))
    const mappedImages = propertyImages.map(image =>(
        
        <Image 
        key = {image.id}
        id = {image.id}
        image = {image.image}
        images = {images}
        setImages = {setImages}
        
        />
       
    ))

    return (
        
        <div className="card-container">
            {mappedImages}
        <button onClick={handleClick} type="button">Add Image</button>
        </div>
        
    )
}
export default Images