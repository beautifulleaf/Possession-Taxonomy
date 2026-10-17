"""Stage-3 data tables (CONVENTIONS_v1, R-58 ids, R-65 and later): one dict, table -> (id column, columns).
Every table ends with sources (one or more fetched URLs, ' | ' separated) and fetch_status (full, partial,
nav-only, failed, excerpt-only; one value per source, same order). tools/data_write.py is the only writer."""

SRC = ["sources", "fetch_status"]

TABLES = {
    # tree
    "kinds": ("kind_id", ["kind_id", "code", "sub_family", "leaf", "name", "native_name", "definition", "sort",
                          "status", "memo_ref", "tested", "notes"] + SRC),
    "nodes": ("node_id", ["node_id", "code", "level", "parent_id", "name", "axis", "sort", "notes"] + SRC),
    # C2 named forms and registers
    "named_forms": ("named_form_id", ["named_form_id", "kind_id", "name", "native_name", "maker_bound", "maker_id",
                                      "line_id", "first_year", "base_named_form_id", "flanker_of", "licensor_id",
                                      "licence_class", "spdx_id", "region", "culture", "register_id", "notes"] + SRC),
    "registers": ("register_id", ["register_id", "kind_id", "name", "scope", "notes"] + SRC),
    # C3 variants
    "variants": ("variant_id", ["variant_id", "named_form_id", "variant_code", "variant_type", "partner", "year",
                                "seat_structure", "seat_count", "eligibility", "term", "price_model", "list_price",
                                "currency", "price_date", "annual_price_usd", "allowances", "components", "addon_of",
                                "status", "notes"] + SRC),
    "concentration_labels": ("label", ["label", "source_name", "pct_min", "pct_max"] + SRC),
    # C1 makers
    "makers": ("maker_id", ["maker_id", "name", "native_name", "maker_class", "supply_role", "country", "place",
                            "founded", "ended", "status", "parent_id", "licensor_id", "authority_id", "school_ids",
                            "extension", "notes"] + SRC),
    "lines": ("line_id", ["line_id", "maker_id", "name", "kinds", "line_rank", "built_by_maker_id", "licensor_id",
                          "years", "notes"] + SRC),
    "maker_relations": ("relation_id", ["relation_id", "maker_id", "other_id", "relation", "scope", "years"] + SRC),
    "schools": ("school_id", ["school_id", "name", "native_name", "tradition", "region", "years"] + SRC),
    "issuers": ("issuer_id", ["issuer_id", "name", "country", "type", "years"] + SRC),
    # C4 tiers and schemes
    "schemes": ("scheme_id", ["scheme_id", "name", "owner", "scale_class", "steps", "direction", "test_version",
                              "stale_after", "kinds_served"] + SRC),
    "tier_entries": ("tier_entry_id", ["tier_entry_id", "subject_id", "subject_type", "scheme_id", "value", "rank",
                                       "direction", "scope", "test_version", "stale_after", "date"] + SRC),
    "prices": ("price_id", ["price_id", "subject_id", "subject_type", "list_price", "currency", "price_date",
                            "usd", "price_band", "unit", "unit_price_band"] + SRC),
    # C8 scenes, C9 aliases
    "scenes": ("scene_id", ["scene_id", "name", "native_name", "domains", "definition_source"] + SRC),
    "scene_tags": ("tag_id", ["tag_id", "subject_id", "subject_type", "scene_id", "strength"] + SRC),
    "aliases": ("alias_id", ["alias_id", "term", "language", "script", "target_id", "relation"] + SRC),
    # C13 compatibility
    "platforms": ("platform_id", ["platform_id", "name", "owner", "platform_type", "kinds_served", "standard_ref",
                                  "region", "introduced", "status", "extension"] + SRC),
    "compatibility": ("compat_id", ["compat_id", "from_id", "relation", "to_id"] + SRC),
    # C16 grading scales, C17 jurisdiction and standards
    "grading_scales": ("scale_id", ["scale_id", "name", "owner", "scale_type", "steps", "kinds_served"] + SRC),
    "jurisdiction": ("jur_id", ["jur_id", "subject_id", "jurisdiction", "scheme", "class", "criteria", "date"] + SRC),
    "standards": ("standard_id", ["standard_id", "name", "authority", "steps"] + SRC),
    "standard_values": ("sv_id", ["sv_id", "subject_id", "standard_id", "value"] + SRC),
    "designations": ("designation_id", ["designation_id", "name", "scheme", "register_ref", "authority", "binds",
                                        "kind_id"] + SRC),
    # domain J
    "varieties": ("variety_id", ["variety_id", "species", "name", "native_name", "holder"] + SRC),
    "culinary_links": ("link_id", ["link_id", "subject_id", "target_code", "relation"] + SRC),
}

FETCH_STATUS = {"full", "partial", "nav-only", "failed", "excerpt-only"}
SUBJECT_TYPES = {"kind", "named_form", "maker", "line", "variant", "plan", "platform"}
