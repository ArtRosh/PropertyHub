import React, {useState} from 'react';



function Review({ name, rating, comment, property, reviews, setReviews, id },){

   
    const [showEditForm, setShowEditForm] = useState(false)
    const [editComment, setEditComment] = useState(comment)
    const [editRating, setEditRating] = useState(rating)
    const [review, setReview] = useState('')
    const handleSubmit = (e) =>{
        
        e.preventDefault();

        const updatedReview = {
            method: "PATCH",
            headers: {
                "Content_Type": "application?json",
            },
            body: JSON.stringify({
                comment : editComment,
                rating : editRating
            }),
            
        };
        console.log(updatedReview)
        fetch(`/reviews/${id}`, updatedReview)
            .then((res) => res.json())
            .then(data => {
                const updatedReviews = reviews.map(review => {
                    if(review.id === data.id){
                        return( data )
                    }else{
                        return( review)
                    }
                })
                setReview(updatedReviews)
                setShowEditForm(false)
            })
            console.log(updatedReview)
    }
    
    function handleDelete(id){
        console.log(id)
        fetch(`/reviews/${id}`,{
            method: "DELETE"
        })
        .then(()=> {
            const filteredReviews = reviews.filter(review =>{
            return (review.id !== id)
        })
        setReviews(filteredReviews)
        console.log(filteredReviews)
        })
    }
    
    if (showEditForm){
        return (
            <div>
                <h3>Edit</h3>
                <form onSubmit = {handleSubmit} review={review}>
                    <input
                    label='Comment'
                    placeholder='Comment'
                    value={editComment}
                    onChange={(e) => setEditComment(e.target.value)}
                    />
                    <input
                    label='Rating'
                    placeholder='Rating'
                    value={rating}
                    onChange={(e) => setEditRating(e.target.value)}
                    />
                    <button type="submit">Submit</button>
                </form>
                <button className='edit_review' onClick={() => setReviews(id)}>Edit</button>
                <button className='delete_review' onClick={() => handleDelete(id)}>Delete</button>
            </div>
        )
    }
    


    return(
        <div className='review-card'>
            <h3>Name:</h3>
            <p>{name}</p>
            <h3>Rating:</h3>
            <p>{rating}</p>
            <h3>Comment:</h3>
            <p>{comment}</p>
            <h3>Property</h3>
            <p>{property}</p>
            <button className='edit_review' onClick={() => setShowEditForm(!showEditForm)}> Edit </button>
            <button className='delete_review' onClick={() => handleDelete(id)}> Delete </button>
        </div>
    )
}
export default Review