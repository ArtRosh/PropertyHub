import React, { useEffect, useState} from "react"
import { useFormik } from "formik"
import * as yup from "yup"
import { useHistory } from "react-router-dom/cjs/react-router-dom"

export const SignupForm = () => {
    const [users, setUsers] = useState([{}])
    const [refreshPage, setRefreshPage] = useState(false)
    const history = useHistory()

    useEffect(() =>{
        console.log("Hey")
        fetch("/users")
            .then(res => res.json())
            .then((data) => {
                setUsers(data)
                
            })
    }, [refreshPage])

    const formSchema = yup.object().shape({
        username: yup.string().required("Invalid Username"),
        password: yup.string().required("Invalid password"),
      });
    console.log(formSchema)
    const formik = useFormik({
        initialValues: {
            username: "",
            password: "",
        },
        validationSchema: formSchema,
        onSubmit: (values, {resetForm}) => {
            fetch("/users", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values, null, 2),
            }).then((res) => {
                if(res.status === 200) {
                    setRefreshPage(!refreshPage);
                    resetForm()
                console.log(values)
                }
                history.push('/')
                console.log(values)
            })
        }
    })

   
    return (
        <div>
            <form onSubmit={formik.handleSubmit}  style={{margin: "30px"}}>
                <label htmlFor='signup'>SignUp</label>
                <br />
                <br />
                Username:
                <input 
                    id="username"
                    name="username"
                    onChange={formik.handleChange}
                    value={formik.values.username}
                />
                Password:
                <input 
                    id="password"
                    name="password"
                    onChange={formik.handleChange}
                    value={formik.values._password_hash}
                />
                <p style={{ color: "red"}}> {formik.errors.username}</p>
                <p style={{ color: "red"}}> {formik.errors.password}</p>
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}
export default SignupForm