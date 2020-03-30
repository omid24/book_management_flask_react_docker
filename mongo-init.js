db.createUser(
    {
        user: "omides",
        pwd: "omides123",
        roles: [
            {
                role: "readWrite",
                db: "omides_money_management_db"
            }
        ]
    }
);