import React from 'react';
import { useHistory } from 'react-router-dom';





function Property({name, location, description, amenities, availability, image, properties, setProperties, reservation, setImages, setReviews, setReview, id}){

    const history = useHistory();

    const handleClick1 =() => {
        history.push(`/properties/${id}/images`)
    }

    const handleClick2 =() => {
        history.push(`/properties/${id}/reviews`)
    }

    const handleClick3 =() => {
        history.push("/newreview")
    }

    
    function handleDelete(id){
    
    fetch(`/properties/${id}`, {
            method: "DELETE"
        })
        .then(() => {
            const filteredProperties = properties.filter(property => {
        
            return (property.id !== id)
        })
        setProperties(filteredProperties)
        })

    }
    if('Admin')
    return (
        <div className='property-container'>
            <p className='property-name'>{name}</p>
            <img className='property-img' src = {image} alt = {name}/>
            <h2>Location</h2>
            <p>{location}</p>
            <h2>Description</h2>
            <p>{description}</p>
            <h2>Amnenties</h2>
            <p>{amenities}</p>
            <button className='rounded-button button-font'>
            <a href={reservation} >Reserve</a>
            </button>
            <br/>
            <br/>
            <button className='delete_property' onClick={() => handleDelete(id)}>Delete</button>
            <br/>
            <br/>
            <button className='images-button ' onClick={handleClick1} type="button">Images</button>
            <br/>
            <br/>
            <button className='reviews-button ' onClick={handleClick2} type="button">Reviews</button>
            <br/>
            <br/>
            <button className='review-button ' onClick={handleClick3} type="button">Please Leave A Review</button>

        </div>
    );
    else
    return (
        <div className='property-container'>
            <p className='property-name'>{name}</p>
            <img className='property-img' src = {image} alt = {name}/>
            <h2>Location</h2>
            <p>{location}</p>
            <h2>Description</h2>
            <p>{description}</p>
            <h2>Amnenties</h2>
            <p>{amenities}</p>
            <button className='rounded-button button-font'>
            <a href={reservation} >Reserve</a>
            </button>
            <br/>
            <br/>
            <br/>
            <br/>
            <button className='images-button ' onClick={handleClick1} type="button">Images</button>
            <br/>
            <br/>
            <button className='reviews-button ' onClick={handleClick2} type="button">Reviews</button>
            <br/>
            <br/>
            <button className='review-button ' onClick={handleClick3} type="button">Please Leave A Review</button>

        </div>
        )
}
export default Property