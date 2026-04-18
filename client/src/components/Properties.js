import React from 'react';
import Property from './Property'
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';

function Properties({properties, setProperties, setImages, setReviews}){

    const history = useHistory()

    const handleClick = () => {
        history.push('/newproperty')
    }
    console.log(properties)
    const mappedProperties = properties.map(property => (
    
        <Property
        key = {property.id}
        id = {property.id}
        name = {property.name}
        location = {property.location}
        description = {property.description}
        amenities = {property.amenities}
        image = {property.image}
        reservation = {property.reservation}
        property = {property}
        properties = {properties}
        setProperties={setProperties}
        setImages={setImages}
        setReviews={setReviews}
        />

    ))

    return (
        <div>
            {mappedProperties}
            <button onClick={handleClick} type="button">Add A Property</button>
        </div>
    )
}
export default Properties