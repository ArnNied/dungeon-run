class BaseEntity:
    """
    Basic entity class.
    """

    __divider = ": "  # Divider between verbose name and value of a property.
    __separator = "    "  # Separator between each property in the same row.

    visible_prop = [
        {
            # "Name": "name",
        },
    ]

    def stringify_prop(self) -> str:
        rows = []
        for props in self.visible_prop:
            row = [
                f"{prop_key}{self.__divider}{getattr(self, prop_val)}"
                for prop_key, prop_val in props.items()
            ]

            rows.append(self.__separator.join(row))

        return "\n".join(rows)
