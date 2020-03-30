import React, {useState} from "react";

import "./add-wallet.css"
import WalletList from "./WalletList";

const AddWallet = () => {

    const [name, setName] = useState("")
    const [budgetAmount, setBudgetAmount] = useState("")
    const [accountNumber, setAccountNumber] = useState("")
    const [error, setError] = useState(false)
    const [success, setSuccess] = useState(false)
    const [added, setAdded] = useState(false)


    const addWalletSubmitHandler = async event => {
        event.preventDefault();

        try {
            console.log("Try")
            const response = await fetch("http://127.0.0.1:5000/users/wallet", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    name: name,
                    budget_amount: budgetAmount,
                    account_number: accountNumber
                })
            })

            if(response.status === 404 || response.status === 500) {
                setError(true)
                setSuccess(false)
                setAdded(false)
                console.log("404 or 500")
            } else {
                setError(false)
                setSuccess(true)
                setAdded(true)
                setAdded(false)
            }


        }catch (e) {
            setError(true)
            setSuccess(false)
            setAdded(false)
            console.log("Catch ", e)
        }

        console.log("set default empty field")

        setName("")
        setBudgetAmount("")
        setAccountNumber("")
    };

    return (

        <div className="container">
            {error && <div className="error">Error server</div> }
            {success && <div className="success">Success server</div> }
            <form onSubmit={addWalletSubmitHandler}>
                <label htmlFor="name">نام کیف پول</label><br/>
                <input
                    id="name"
                    type="text"
                    placeholder="نام کیف پول را اینجا وارد کنید"
                    required
                    value={name}
                    onChange={e => {setName(e.target.value)}}
                /><br/>
                <label htmlFor="budget-amount">مقدار کیف پول</label><br/>
                <input
                    id="budget-amount"
                    type="number"
                    placeholder="مقدار کیف پول را اینجا وارد کنید"
                    required
                    value={budgetAmount}
                    min="0"
                    onChange={e => {setBudgetAmount(e.target.value)}}
                /><br/>
                <label htmlFor="account-number">شماره حساب</label><br/>
                <input
                    id="account-number"
                    type="text"
                    placeholder="شماره حساب را اینجا وارد کنید"
                    required
                    pattern="\b^(\d{4}|(\d-?){4}|(\d\s?){4}){4}\b"
                    value={accountNumber}
                    onChange={e => {setAccountNumber(e.target.value)}}
                /><br/>
                <button type="submit" >افزودن کیف پول</button>
            </form>
            <WalletList added={added}/>
        </div>

    );
}

export default AddWallet;