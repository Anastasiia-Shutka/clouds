from flask import Blueprint
from my_project.sportsman.controller.orders.coaches_contact_controller import CoachesContactController

coaches_contact_bp = Blueprint("coaches_contact", __name__)
coaches_contact_controller = CoachesContactController()


@coaches_contact_bp.route("/coaches_contact", methods=['GET'])
def get_coaches_contact():
    """
    Get all coaches contacts
    ---
    tags:
      - CoachesContact
    responses:
      200:
        description: A list of coaches contacts
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  phone:
                    type: string
                    example: "+123456789"
                  email:
                    type: string
                    example: "coach@email.com"
    """
    return coaches_contact_controller.get_all()


@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['GET'])
def get_coaches_contact_by_id(coaches_contact_id):
    """
    Get a coach's contact by ID
    ---
    tags:
      - CoachesContact
    parameters:
      - name: coaches_contact_id
        in: path
        schema:
          type: integer
        required: true
        description: ID of the coach contact
    responses:
      200:
        description: Coach contact found
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                phone:
                  type: string
                  example: "+123456789"
                email:
                  type: string
                  example: "coach@email.com"
      404:
        description: Coach contact not found
    """
    return coaches_contact_controller.get_by_id(coaches_contact_id)


@coaches_contact_bp.route("/coaches_contact", methods=['POST'])
def add_coaches_contact():
    """
    Create a new coach contact
    ---
    tags:
      - CoachesContact
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - phone
              - email
            properties:
              phone:
                type: string
                example: "+123456789"
              email:
                type: string
                example: "coach@email.com"
    responses:
      201:
        description: Coach contact created
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                phone:
                  type: string
                  example: "+123456789"
                email:
                  type: string
                  example: "coach@email.com"
    """
    return coaches_contact_controller.create()


@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['PATCH'])
def update_coaches_contact(coaches_contact_id):
    """
    Update a coach contact
    ---
    tags:
      - CoachesContact
    parameters:
      - name: coaches_contact_id
        in: path
        schema:
          type: integer
        required: true
        description: ID of the coach contact to update
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              phone:
                type: string
                example: "+987654321"
              email:
                type: string
                example: "newcoach@email.com"
    responses:
      200:
        description: Coach contact updated
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                phone:
                  type: string
                  example: "+987654321"
                email:
                  type: string
                  example: "newcoach@email.com"
      404:
        description: Coach contact not found
    """
    return coaches_contact_controller.update(coaches_contact_id)


@coaches_contact_bp.route("/coaches_contact/<int:coaches_contact_id>", methods=['DELETE'])
def delete_coaches_contact(coaches_contact_id):
    """
    Delete a coach contact
    ---
    tags:
      - CoachesContact
    parameters:
      - name: coaches_contact_id
        in: path
        schema:
          type: integer
        required: true
        description: ID of the coach contact to delete
    responses:
      200:
        description: Coach contact deleted
      404:
        description: Coach contact not found
    """
    return coaches_contact_controller.delete(coaches_contact_id)
