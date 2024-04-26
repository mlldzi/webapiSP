from flask import Blueprint, jsonify, request
from models.company import Company
from database.db import db
import uuid

company_controller = Blueprint('company', __name__)


@company_controller.route('/companies', methods=['POST'])
def create_company():
    data = request.get_json()
    new_company = Company(
        id=str(uuid.uuid4()),
        name=data['name'],
        big_boss=data['big_boss'],
        country=data['country']
    )
    db.session.add(new_company)
    db.session.commit()
    return jsonify({"message": "Company created successfully.", "company_id": new_company.id}), 201


@company_controller.route('/companies/<company_id>', methods=['GET'])
def get_company(company_id):
    company = Company.query.filter_by(id=company_id).first()
    if company:
        return jsonify(
            {"id": company.id, "name": company.name, "big_boss": company.big_boss, "country": company.country}), 200
    return jsonify({"message": "Company not found"}), 404
