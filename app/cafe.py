import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        can_visit_cafe = True
        current_visitor = visitor.get("vaccine", False)
        expiry = current_visitor.get(
            "expiration_date", False
        ) if current_visitor else False

        if not current_visitor:
            can_visit_cafe = False
            raise NotVaccinatedError(f"{visitor['name']} is not vaccinated")
        if expiry:
            today = datetime.date.today()
            if today > expiry:
                can_visit_cafe = False
                raise OutdatedVaccineError(
                    f"Vaccine of {visitor['name']} is outdated"
                )
        if not visitor.get("wearing_a_mask", False):
            can_visit_cafe = False
            raise NotWearingMaskError(
                f"{visitor['name']} is not wearing a mask"
            )

        if can_visit_cafe:
            return f"Welcome to {self.name}"
