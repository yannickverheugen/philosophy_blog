def test_contact_form_user_flow(client):
    home_response = client.get("/")
    assert home_response.status_code == 200

    contact_page_response = client.get("/contact")
    assert contact_page_response.status_code == 200

    submit_response = client.post(
        "/contact",
        data={
            "user_name": "Sophie",
            "user_email": "sophie@example.com",
            "user_message": "Please share more stoicism articles.",
        },
    )

    assert submit_response.status_code == 200
    assert b"Thank you Sophie for your message" in submit_response.data
    assert b"We will contact you at sophie@example.com." in submit_response.data