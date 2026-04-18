import React, { useState, useContext } from 'react';
import {useHistory} from "react-router-dom"
import { DarkModeContext } from './DarkModeContext';

function NewPropertyForm({setProperties}){

   const { isDarkMode } = useContext(DarkModeContext)

    const [name, setName] = useState("")
    const [location, setLocation] = useState("")
    const [description, setDescription] = useState("")
    const [image, setImage] = useState("")
    const [amenities, setAmenities] = useState("")
    const [availability, setAvailability] = useState("")
    const [reservation, setReservation] = useState("")
    const history = useHistory()

    const handleSubmit = (e) => {
        e.preventDefault();


    const propertyForm = {
        method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name,
                location,
                description,
                amenities,
                availability,
                image,
                reservation,
            })
        };
        fetch(`/properties`, propertyForm)
            .then((res) => res.json())
            .then((data) => {
                setProperties( properties => [...properties, data])
                history.push('/properties')
})
            
            setName("");
            setLocation("");
            setDescription("");
            setAmenities("");
            setAvailability("");
            setImage("");
        }


    return (
        <div className={isDarkMode ? 'dark' : 'light'}>
            

            <form className="form-container" onSubmit={handleSubmit}>
                <h3>Add a Property</h3>
                <input
                label='Name'
                placeholder='Name'
                value={name}
                onChange={(e) => setName(e.target.value)}
                />
                <input
                label='Location'
                placeholder='Location'
                value={location}
                onChange={(e) => setLocation(e.target.value)}
                /><input
                label='Description'
                placeholder='Description'
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                /><input
                label='Amenities'
                placeholder='Amentiies'
                value={amenities}
                onChange={(e) => setAmenities(e.target.value)}
                /><input
                label='Availability'
                placeholder='Availability'
                value={availability}
                onChange={(e) => setAvailability(e.target.value)}
                /><input
                label='Image'
                placeholder='Image'
                value={image}
                onChange={(e) => setImage(e.target.value)}
                />
                <input
                label='Reservation'
                placeholder='Reservation'
                value={reservation}
                onChange={(e) => setReservation(e.target.value)}
                />
                <button className='add_property'>Add a Property</button>
            </form>
           
        </div>
    )
    
}
export default NewPropertyForm