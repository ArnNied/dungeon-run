from dungeonrun.prop import Prop


class BaseEntity:
    """
    Basic entity class.
    """

    name = Prop("")

    visible_prop = [
        {
            "Name": "name",
        },
    ]

    def stringify_prop(self) -> str:
        rows = []
        for props in self.visible_prop:
            row = [
                f"{prop_key}: {getattr(self, prop_val)}"
                for prop_key, prop_val in props.items()
            ]

            rows.append("    ".join(row))

        return "\n".join(rows)
