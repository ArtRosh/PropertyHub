import React from 'react';
import Review from './Review';
import { useParams } from 'react-router-dom/cjs/react-router-dom.min';
function Reviews({reviews, setReviews}){
    let {id} = useParams()
    const propertyReviews = reviews.filter(review => review.property_id === parseInt(id))
    const mappedReviews = propertyReviews.map(review => (
       <Review
       key = {review.id}
       id = {review.id}
       name = {review.name}
       rating = {review.rating}
       comment = {review.comment}
       property = {review.property.name}
       review = {review}
       reviews = {reviews}
       setReviews= {setReviews}
       />
        
    ))
    console.log(mappedReviews)
    return (
        <div className='review-container'>
            {mappedReviews}
        </div>
    )
}
export default Reviews