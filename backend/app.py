from flask import Flask, request, jsonify, send_from_directory
from models import *
from flask_cors import CORS
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"
app.config['SECRET_KEY'] = "anuragiitmadras"

db.init_app(app)
jwt = JWTManager(app)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # 465  # SSL Port
SMTP_USERNAME = 'akanuragkumar75@gmail.com'  # Replace with your email
SMTP_PASSWORD = 'gersqaguuxkhotwt'  # Replace with your email password


def insert_dummy_data():
    users_data = [
        {"email": "tech@kvqaindia.com",
         "username": "tech@kvqaindia", "password": "asdfgh"},
        {"email": "akanuragkumar4@gmail.com",
         "username": "anuragkumar", "password": "qwerty"}
    ]

    # with app.app_context():
    #     for data in users_data:
    #         existing_user = User.query.filter_by(email=data['email']).first()
    #         if not existing_user:
    #             user = User(email=data['email'], username=data['username'])
    #             user.password_hash = generate_password_hash(
    #                 data['password'])
    #             db.session.add(user)

    with app.app_context():
        for data in users_data:
            existing_user = User.query.filter_by(email=data['email']).first()
            if not existing_user:
                user = User(email=data['email'], username=data['username'])
                user.set_password(data['password'])  # ✅ Use set_password()
                db.session.add(user)

        db.session.commit()


@app.route('/')
def home():
    return "App Started!"


# @app.route('/get')
# def user_get():
#     users = User.query.all()
#     user_list = [
#         {"id": user.id, "email": user.email,
#             "username": user.username, "password": user.password_hash}
#         for user in users
#     ]
#     return jsonify(user_list), 200


@app.route('/get', methods=['GET'])
@jwt_required()
def user_get():
    # Get logged-in user's email
    current_user_email = get_jwt_identity()['email']
    users = User.query.filter_by(
        email=current_user_email).all()  # Fetch only their data
    user_list = [
        {"id": user.id, "email": user.email, "username": user.username}
        for user in users
    ]
    return jsonify(user_list), 200


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # print("Email: ", email)
    # print("Password: ", password)

    user = User.query.filter_by(email=email).first()
    # ✅ Compare with check_password()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.email)
        return jsonify({'token': access_token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401


# @app.route('/stage1', methods=['POST'])
# def submit_stage1():
#     try:
#         data = request.form  # Get form data

#         # Handle file uploads
#         stage1_plan = request.files.get("stage1Plan")
#         stage1_report = request.files.get("stage1Report")

#         # Save uploaded files to a directory
#         upload_folder = "uploads/"
#         os.makedirs(upload_folder, exist_ok=True)

#         plan_filename = os.path.join(
#             upload_folder, stage1_plan.filename) if stage1_plan else None
#         report_filename = os.path.join(
#             upload_folder, stage1_report.filename) if stage1_report else None

#         if stage1_plan:
#             stage1_plan.save(plan_filename)
#         if stage1_report:
#             stage1_report.save(report_filename)

#         # Create a new Stage1 record in the database
#         new_stage1 = Stage1(
#             organisation_name=data.get("organisationName"),
#             scope=data.get("scope"),
#             stage1_plan=plan_filename,
#             mail_from=data.get("mailFrom"),
#             mail_to=data.get("mailTo"),
#             selected_date=data.get("selectedDate"),
#             selected_comment_date=data.get("selectedCommentDate"),
#             stage1_report=report_filename,
#             comment=data.get("comment"),
#         )

#         db.session.add(new_stage1)
#         db.session.commit()

#         return jsonify({"message": "Stage 1 form submitted successfully"}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


@app.route('/stage1', methods=['POST'])
@jwt_required()
def submit_stage1():
    try:
        data = request.form
        current_user_email = get_jwt_identity()
        user = User.query.filter_by(email=current_user_email).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        # Handle file uploads
        stage1_plan = request.files.get("stage1Plan")
        stage1_report = request.files.get("stage1Report")

        upload_folder = "uploads/"
        os.makedirs(upload_folder, exist_ok=True)

        plan_filename = os.path.join(
            upload_folder, stage1_plan.filename) if stage1_plan else None
        report_filename = os.path.join(
            upload_folder, stage1_report.filename) if stage1_report else None

        if stage1_plan:
            stage1_plan.save(plan_filename)
        if stage1_report:
            stage1_report.save(report_filename)

        # Store user_id with the stage1 record
        new_stage1 = Stage1(
            user_id=user.id,  # ✅ Store user ID
            organisation_name=data.get("organisationName"),
            scope=data.get("scope"),
            stage1_plan=plan_filename,
            mail_from=data.get("mailFrom"),
            mail_to=data.get("mailTo"),
            selected_date=data.get("selectedDate"),
            selected_comment_date=data.get("selectedCommentDate"),
            stage1_report=report_filename,
            comment=data.get("comment"),
        )

        db.session.add(new_stage1)
        db.session.commit()

        return jsonify({"message": "Stage 1 form submitted successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# @app.route('/stage2', methods=['POST'])
# def submit_stage2():
#     try:
#         data = request.form  # Get form data

#         # Handle file uploads
#         stage2_plan = request.files.get("stage2Plan")
#         stage2_report = request.files.get("stage2Report")

#         # Save uploaded files to a directory
#         upload_folder = "uploads/"
#         os.makedirs(upload_folder, exist_ok=True)

#         plan_filename = os.path.join(
#             upload_folder, stage2_plan.filename) if stage2_plan else None
#         report_filename = os.path.join(
#             upload_folder, stage2_report.filename) if stage2_report else None

#         if stage2_plan:
#             stage2_plan.save(plan_filename)
#         if stage2_report:
#             stage2_report.save(report_filename)

#         # Create a new Stage1 record in the database
#         new_stage2 = Stage2(
#             organisation_name=data.get("organisationName"),
#             scope=data.get("scope"),
#             stage2_plan=plan_filename,
#             mail_from=data.get("mailFrom"),
#             mail_to=data.get("mailTo"),
#             selected_date=data.get("selectedDate"),
#             selected_comment_date=data.get("selectedCommentDate"),
#             stage2_report=report_filename,
#             comment=data.get("comment"),
#         )

#         db.session.add(new_stage2)
#         db.session.commit()

#         return jsonify({"message": "Stage 2 form submitted successfully"}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


@app.route('/stage2', methods=['POST'])
@jwt_required()
def submit_stage2():
    try:
        data = request.form
        user_email = get_jwt_identity()
        user = User.query.filter_by(email=user_email).first()

        stage2_plan = request.files.get("stage2Plan")
        stage2_report = request.files.get("stage2Report")

        upload_folder = "uploads/"
        os.makedirs(upload_folder, exist_ok=True)

        plan_filename = os.path.join(
            upload_folder, stage2_plan.filename) if stage2_plan else None
        report_filename = os.path.join(
            upload_folder, stage2_report.filename) if stage2_report else None

        if stage2_plan:
            stage2_plan.save(plan_filename)
        if stage2_report:
            stage2_report.save(report_filename)

        new_stage2 = Stage2(
            organisation_name=data.get("organisationName"),
            scope=data.get("scope"),
            stage2_plan=plan_filename,
            mail_from=data.get("mailFrom"),
            mail_to=data.get("mailTo"),
            selected_date=data.get("selectedDate"),
            selected_comment_date=data.get("selectedCommentDate"),
            stage2_report=report_filename,
            comment=data.get("comment"),
            user_id=user.id  # Associate with logged-in user
        )

        db.session.add(new_stage2)
        db.session.commit()

        return jsonify({"message": "Stage 2 form submitted successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# @app.route('/dashboard', methods=['POST'])
# def dashboard_data():
#     try:
#         data = request.get_json()

#         new_application = Dashboard(
#             org_name=data.get("org_name"),
#             audit_number=data.get("audit_number"),
#             auditor=data.get("auditor"),
#             decision_maker=data.get("decision_maker"),
#             status="Pending"  # Default status for new applications
#         )

#         db.session.add(new_application)
#         db.session.commit()

#         return jsonify({"message": "Application added successfully"}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


@app.route('/dashboard', methods=['POST'])
@jwt_required()
def dashboard_data():
    try:
        data = request.get_json()
        user_email = get_jwt_identity()
        user = User.query.filter_by(email=user_email).first()

        new_application = Dashboard(
            org_name=data.get("org_name"),
            audit_number=data.get("audit_number"),
            auditor=data.get("auditor"),
            decision_maker=data.get("decision_maker"),
            status="Pending",
            user_id=user.id  # Associate with logged-in user
        )

        db.session.add(new_application)
        db.session.commit()

        return jsonify({"message": "Application added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# @app.route('/dashboard', methods=['GET'])
# def get_dashboard_data():
#     try:
#         applications = Dashboard.query.all()
#         data = [
#             {
#                 "id": app.id,
#                 "org_name": app.org_name,
#                 "audit_number": app.audit_number,
#                 "status": app.status,
#                 "auditor": app.auditor,
#                 "decision_maker": app.decision_maker,
#             }
#             for app in applications
#         ]
#         return jsonify(data), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

@app.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard_data():
    try:
        current_user_email = get_jwt_identity()
        print("Decoded JWT Identity:", current_user_email)  # ✅ Debugging

        user = User.query.filter_by(email=current_user_email).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        applications = Dashboard.query.filter_by(user_id=user.id).all()
        data = [{"id": app.id, "org_name": app.org_name, "audit_number": app.audit_number, "status": app.status,
                 "auditor": app.auditor, "decision_maker": app.decision_maker} for app in applications]

        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# @app.route('/dashboard/<int:id>', methods=['DELETE'])
# def delete_application(id):
#     try:
#         application = Dashboard.query.get(id)
#         if not application:
#             return jsonify({"error": "Application not found"}), 404

#         db.session.delete(application)
#         db.session.commit()
#         return jsonify({"message": "Application deleted successfully"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


@app.route('/dashboard/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_application(id):
    try:
        user_email = get_jwt_identity()
        user = User.query.filter_by(email=user_email).first()

        application = Dashboard.query.filter_by(id=id, user_id=user.id).first()
        if not application:
            return jsonify({"error": "Application not found or unauthorized"}), 404

        db.session.delete(application)
        db.session.commit()
        return jsonify({"message": "Application deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/send-email', methods=['POST'])
def send_email():
    mail_to = request.form.get("mailTo")
    subject = request.form.get("subject")
    body = request.form.get("body")

    if not mail_to:
        return jsonify({"message": "Recipient email is required!"}), 400

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SMTP_USERNAME  # Sender email
    msg["To"] = mail_to
    msg.set_content(body)

    # Attach uploaded files (if any)
    attachments = request.files.getlist("attachments")
    for file in attachments:
        msg.add_attachment(file.read(), maintype="application",
                           subtype="octet-stream", filename=file.filename)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Authenticate
            server.send_message(msg)

        return jsonify({"message": f"Email sent successfully to {mail_to}!"}), 200

    except Exception as e:
        return jsonify({"message": f"Failed to send email: {str(e)}"}), 500


# @app.route("/application/<string:organisation_name>", methods=["GET"])
# def get_application_details(organisation_name):
#     try:
#         stage1_data = Stage1.query.filter_by(organisation_name=organisation_name).first()
#         stage2_data = Stage2.query.filter_by(organisation_name=organisation_name).first()

#         if not stage1_data and not stage2_data:
#             return jsonify({"message": "No data found"}), 404

#         return jsonify({
#             "stage1": {
#                 "id": stage1_data.id if stage1_data else None,
#                 "scope": stage1_data.scope if stage1_data else None,
#                 "stage1_plan": stage1_data.stage1_plan if stage1_data else None,
#                 "mail_from": stage1_data.mail_from if stage1_data else None,
#                 "mail_to": stage1_data.mail_to if stage1_data else None,
#                 "selected_date": stage1_data.selected_date if stage1_data else None,
#                 "selected_comment_date": stage1_data.selected_comment_date if stage1_data else None,
#                 "stage1_report": stage1_data.stage1_report if stage1_data else None,
#                 "comment": stage1_data.comment if stage1_data else None
#             },
#             "stage2": {
#                 "id": stage2_data.id if stage2_data else None,
#                 "scope": stage2_data.scope if stage2_data else None,
#                 "stage2_plan": stage2_data.stage2_plan if stage2_data else None,
#                 "mail_from": stage2_data.mail_from if stage2_data else None,
#                 "mail_to": stage2_data.mail_to if stage2_data else None,
#                 "selected_date": stage2_data.selected_date if stage2_data else None,
#                 "selected_comment_date": stage2_data.selected_comment_date if stage2_data else None,
#                 "stage2_report": stage2_data.stage2_report if stage2_data else None,
#                 "comment": stage2_data.comment if stage2_data else None
#             }
#         }), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


@app.route("/application/<string:organisation_name>", methods=["GET"])
@jwt_required()
def get_application_details(organisation_name):
    try:
        user_email = get_jwt_identity()
        user = User.query.filter_by(email=user_email).first()

        # Ensure the user can only access their own applications
        stage1_data = Stage1.query.filter_by(
            organisation_name=organisation_name, user_id=user.id).first()
        stage2_data = Stage2.query.filter_by(
            organisation_name=organisation_name, user_id=user.id).first()

        if not stage1_data and not stage2_data:
            return jsonify({"message": "No data found or unauthorized access"}), 404

        return jsonify({
            "stage1": {
                "id": stage1_data.id if stage1_data else None,
                "scope": stage1_data.scope if stage1_data else None,
                "stage1_plan": stage1_data.stage1_plan if stage1_data else None,
                "mail_from": stage1_data.mail_from if stage1_data else None,
                "mail_to": stage1_data.mail_to if stage1_data else None,
                "selected_date": stage1_data.selected_date if stage1_data else None,
                "selected_comment_date": stage1_data.selected_comment_date if stage1_data else None,
                "stage1_report": stage1_data.stage1_report if stage1_data else None,
                "comment": stage1_data.comment if stage1_data else None
            },
            "stage2": {
                "id": stage2_data.id if stage2_data else None,
                "scope": stage2_data.scope if stage2_data else None,
                "stage2_plan": stage2_data.stage2_plan if stage2_data else None,
                "mail_from": stage2_data.mail_from if stage2_data else None,
                "mail_to": stage2_data.mail_to if stage2_data else None,
                "selected_date": stage2_data.selected_date if stage2_data else None,
                "selected_comment_date": stage2_data.selected_comment_date if stage2_data else None,
                "stage2_report": stage2_data.stage2_report if stage2_data else None,
                "comment": stage2_data.comment if stage2_data else None
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# @app.route("/download/<path:filename>", methods=["GET"])
# def download_file(filename):
#     try:
#         return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 404


# @app.route("/download/<path:filename>", methods=["GET"])
# @jwt_required()
# def download_file(filename):
#     try:
#         user_email = get_jwt_identity()
#         user = User.query.filter_by(email=user_email).first()

#         # Ensure only filename is checked (without "uploads/")
#         filename = filename.replace("uploads/", "")

#         # Check if file belongs to the user
#         stage1_file = Stage1.query.filter(
#             (Stage1.stage1_plan == filename) | (Stage1.stage1_report == filename),
#             Stage1.user_id == user.id
#         ).first()
#         stage2_file = Stage2.query.filter(
#             (Stage2.stage2_plan == filename) | (Stage2.stage2_report == filename),
#             Stage2.user_id == user.id
#         ).first()

#         if not stage1_file and not stage2_file:
#             return jsonify({"error": "File not found or unauthorized access"}), 403

#         upload_folder = "uploads"  # Ensure this matches your actual upload directory
#         return send_from_directory(upload_folder, filename, as_attachment=True)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 404


@app.route("/download/<path:filename>", methods=["GET"])
@jwt_required()
def download_file(filename):
    try:
        user_email = get_jwt_identity()
        user = User.query.filter_by(email=user_email).first()

        # Ensure correct filename format
        filename = filename.replace("uploads/", "")

        print(f"Requested file: {filename}")
        print(f"Logged-in user: {user_email} (User ID: {user.id})")

        # Debug: Check what filenames exist in the database
        user_files_stage1 = Stage1.query.filter(
            Stage1.user_id == user.id).all()
        user_files_stage2 = Stage2.query.filter(
            Stage2.user_id == user.id).all()

        print(
            f"User's Stage 1 Files: {[file.stage1_plan for file in user_files_stage1]}")
        print(
            f"User's Stage 2 Files: {[file.stage2_plan for file in user_files_stage2]}")

        # Check if file belongs to the user
        stage1_file = Stage1.query.filter(
            (Stage1.stage1_plan == f"uploads/{filename}") | (
                Stage1.stage1_report == f"uploads/{filename}"),
            Stage1.user_id == user.id
        ).first()
        stage2_file = Stage2.query.filter(
            (Stage2.stage2_plan == f"uploads/{filename}") | (
                Stage2.stage2_report == f"uploads/{filename}"),
            Stage2.user_id == user.id
        ).first()

        if not stage1_file and not stage2_file:
            print("Unauthorized file access attempt.")
            return jsonify({"error": "File not found or unauthorized access"}), 403

        upload_folder = "uploads"
        return send_from_directory(upload_folder, filename, as_attachment=True)

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 404


@app.route('/search', methods=['GET'])
@jwt_required()
def search_dashboard():
    # Get the authenticated user's email from JWT
    user_email = get_jwt_identity()
    print(f"🔹 JWT Identity (Email): {user_email}")

    # Fetch user by email
    user = User.query.filter_by(email=user_email).first()
    if not user:
        print(f"❌ No user found with email: {user_email}")
        return jsonify({"error": "User not found"}), 400

    user_id = user.id
    print(f"✅ Retrieved User ID: {user_id}")

    # Get search parameters
    org_name = request.args.get("org_name", "").strip()
    audit_number = request.args.get("audit_number", "").strip()
    print(
        f"🔍 Search Parameters - Org: '{org_name}', Audit: '{audit_number}', User ID: {user_id}")

    # Build search query
    query = Dashboard.query.filter(Dashboard.user_id == user_id)

    if org_name:
        query = query.filter(Dashboard.org_name.ilike(f"%{org_name}%"))
        print(f"✅ Applied filter for org_name: {org_name}")

    if audit_number:
        query = query.filter(Dashboard.audit_number.ilike(f"%{audit_number}%"))
        print(f"✅ Applied filter for audit_number: {audit_number}")

    # Execute query
    results = query.all()
    print(f"✅ Query Results: {results}")

    # Format response
    applications = [
        {
            "id": app.id,
            "org_name": app.org_name,
            "audit_number": app.audit_number,
            "auditor": app.auditor,
            "decision_maker": app.decision_maker,
            "status": app.status,
        }
        for app in results
    ]

    return jsonify(applications), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        insert_dummy_data()
        app.run(debug="True")
