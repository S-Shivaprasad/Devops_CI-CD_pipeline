def analyze_pipeline(pipeline):
    analysis = {
        "job_count": 0,
        "long_running_steps": [],
        "parallel_jobs": False,
    }

    jobs = pipeline.get("jobs", {})
    analysis["job_count"] = len(jobs)

    for job_name, job_data in jobs.items():
        steps = job_data.get("steps", [])
        for step in steps:
            name = step.get("name", "")
            if "timeout-minutes" in job_data and job_data["timeout-minutes"] > 10:
                analysis["long_running_steps"].append(name)

        if job_data.get("strategy", {}).get("matrix"):
            analysis["parallel_jobs"] = True

    return analysis
