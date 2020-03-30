import React, {useEffect, useState} from "react";
import DeleteIcon from '@material-ui/icons/Delete';

import "./wallet-list.css"

const WalletList = props => {

    const [loadedWallets, setLoadedWallet] = useState()
    const [deleted, setDeleted] = useState(false)

    useEffect(() => {
        const sendRequest = async () => {
            try {
                const response = await fetch("http://127.0.0.1:5000/users/wallet")
                const responseData = await response.json()
                console.log(responseData)
                setLoadedWallet(responseData)

                if (!response.ok) {
                    throw new Error(responseData.message)
                }
            } catch (e) {
                console.log(e)
            }

        }
        sendRequest()
    }, [props.success, deleted])

    const deleteHandler = async _id => {

        try {
            console.log("Try with _id: ", _id)
            const response = await fetch("http://127.0.0.1:5000/users/wallet", {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({_id})
            })

            console.log(response)
            setDeleted(true)
            setDeleted(false)


        }catch (e) {
            console.log("Catch ", e)
        }

        console.log("deleted with id: ", _id)
    }

    return (
        <div className="container">
            <table>
                <tbody>
                <tr>
                    <th>نام کیف پول</th>
                    <th>مقدار کیف پول</th>
                    <th>شماره حساب</th>
                    <th>حذف</th>
                </tr>

                {loadedWallets && loadedWallets.map(wallet => (
                    <tr key={wallet._id}>
                        <td>{wallet.name}</td>
                        <td>{wallet.budget_amount}</td>
                        <td>{wallet.account_number}</td>
                        <td><DeleteIcon onClick={() => {deleteHandler(wallet._id)}} style={{color: "#dc3545"}}/></td>
                    </tr>
                ))}

                </tbody>
            </table>

        </div>
    )
};


export default WalletList;

