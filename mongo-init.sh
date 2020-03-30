mongo -- "$MONGO_INITDB_DATABASE" <<EOF
    var rootUser = 'root';
    var rootPassword = 'pass';
    var admin = db.getSiblingDB('admin');
    admin.auth(rootUser, rootPassword);

    var user = 'omides';
    var passwd = '123';
    db.createUser({user: user, pwd: passwd, roles: ["readWrite"]});
EOF