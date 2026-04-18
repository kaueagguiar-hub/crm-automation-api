from flasgger import Swagger
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

Swagger(app)
db = SQLAlchemy(app)


# =========================
# MODEL
# =========================
class Lead(db.Model):
    __tablename__ = "leads"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100))
    interest = db.Column(db.String(200))
    priority = db.Column(db.String(20), default="medium")
    status = db.Column(db.String(20), default="new")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# =========================
# ROUTES
# =========================

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/leads", methods=["POST"])
def create_lead():
    """
    Criar novo lead
    ---
    tags:
      - Leads
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - email
          properties:
            name:
              type: string
            email:
              type: string
            company:
              type: string
            interest:
              type: string
    responses:
      201:
        description: Lead criado com sucesso
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON inválido"}), 400

    if "name" not in data or "email" not in data:
        return jsonify({"error": "Campos 'name' e 'email' são obrigatórios"}), 400

    priority = "high" if "ia" in data.get("interest", "").lower() else "medium"

    lead = Lead(
        name=data["name"],
        email=data["email"],
        company=data.get("company"),
        interest=data.get("interest"),
        priority=priority
    )

    db.session.add(lead)
    db.session.commit()

    return jsonify({
        "message": "Lead criado com sucesso",
        "lead_id": lead.id
    }), 201


@app.route("/leads", methods=["GET"])
def get_leads():
    """
    Listar todos os leads
    ---
    tags:
      - Leads
    responses:
      200:
        description: Lista de leads
    """
    leads = Lead.query.all()

    result = []
    for lead in leads:
        result.append({
            "id": lead.id,
            "name": lead.name,
            "email": lead.email,
            "company": lead.company,
            "interest": lead.interest,
            "priority": lead.priority,
            "status": lead.status,
            "created_at": lead.created_at
        })

    return jsonify(result), 200


@app.route("/leads/<int:lead_id>/status", methods=["PUT"])
def update_status(lead_id):
    """
    Atualizar status do lead
    ---
    tags:
      - Leads
    parameters:
      - in: path
        name: lead_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            status:
              type: string
    responses:
      200:
        description: Status atualizado com sucesso
    """
    lead = Lead.query.get(lead_id)

    if not lead:
        return jsonify({"error": "Lead não encontrado"}), 404

    data = request.get_json()

    if not data or "status" not in data:
        return jsonify({"error": "Campo 'status' é obrigatório"}), 400

    new_status = data["status"]

    valid_status = ["new", "contacted", "qualified", "closed"]

    if new_status not in valid_status:
        return jsonify({"error": "Status inválido"}), 400

    lead.status = new_status
    db.session.commit()

    return jsonify({"message": "Status atualizado com sucesso"}), 200


@app.route("/metrics", methods=["GET"])
def metrics():
    """
    Obter métricas do funil
    ---
    tags:
      - Metrics
    responses:
      200:
        description: Métricas retornadas com sucesso
    """
    total = Lead.query.count()
    new = Lead.query.filter_by(status="new").count()
    contacted = Lead.query.filter_by(status="contacted").count()
    qualified = Lead.query.filter_by(status="qualified").count()
    closed = Lead.query.filter_by(status="closed").count()
    high_priority = Lead.query.filter_by(priority="high").count()

    return jsonify({
        "total_leads": total,
        "new": new,
        "contacted": contacted,
        "qualified": qualified,
        "closed": closed,
        "high_priority": high_priority
    }), 200


# =========================
# INIT DATABASE
# =========================
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)