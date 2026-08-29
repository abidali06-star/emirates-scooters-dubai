"""
Module: ai_post_generator.py
Generates creative, non-repetitive, topic-tailored social media and ad posts in English & Arabic for Emirates E-Scooters (Mankeel).
"""

from typing import Dict, Any, List

class AIPostGenerator:
    def __init__(self):
        self.delivery_areas_en = "Motor City, Sports City, JVC, Arabian Ranches, Damac Hills, Mudon, Studio City, Al Barsha South, Production City, Green Community, and JVT"
        self.delivery_areas_ar = "موتور سيتي، سبورتس سيتي، قرية جميرا الدائرية، مزارع العرب، دماك هيلز، مدن، ستوديو سيتي، برشاء ساوث، برودكشن سيتي، الجرين كوميونيتي، وقرية جميرا المثلثة"
        self.website_url = "https://emirates-scooters-dubai.vercel.app"

    def generate_post(self, topic: str, target_model: str) -> Dict[str, Any]:
        t_lower = topic.lower()

        # 1. Determine Model Specs & Pricing
        if "mk083" in target_model.lower() and "mx-14" not in target_model.lower():
            model_name = "Mankeel MK083 City Commuter"
            model_slug = "mk083"
            price = "699 AED"
            specs_en = "350W Motor | 25 km/h Top Speed | 30 km Range | Solid Honeycomb Puncture-Proof Tires | 12.3 kg Lightweight Folding"
            specs_ar = "محرك 350 واط | سرعة 25 كم/ساعة | مدى 30 كم | إطارات صلبة مقاومة للثقب 100% | طي خفيف الوزن 12.3 كجم"
        elif "mx-14" in target_model.lower() and "mk083" not in target_model.lower():
            model_name = "Mankeel MX-14 Off-Road Heavy-Duty"
            model_slug = "mx-14"
            price = "1,499 AED"
            specs_en = "800W Peak High-Torque Motor | Dual Rear Spring Suspensions | 56 km Range | 10\" All-Terrain Tires"
            specs_ar = "محرك قوي 800 واط | نظام تعليق خلفي مزدوج | مدى 56 كم | إطارات 10 بوصة للطرق الوعرة"
        else:
            model_name = "Mankeel Electric Scooters (MK083 & MX-14)"
            model_slug = ""
            price = "From 699 AED"
            specs_en = "350W–800W Motor Options | Puncture-Proof Honeycomb Tires | Up to 56 km Range | 1-Year Local Warranty"
            specs_ar = "خيارات محرك 350-800 واط | إطارات صلبة مقاومة للثقب | مدى يصل إلى 56 كم | ضمان محلي سنة"

        # 2. Dynamic Campaign Hooks & Angles
        if any(w in t_lower for w in ["school", "campus", "student", "university", "education", "college"]):
            title_en = f"🎓 Back to Campus: {model_name} ({price})"
            title_ar = f"🎓 العودة للمدارس والجامعات: سكوتر {model_name} ({price})"
            hook_en = f"Ditch traffic and expensive rides for your daily school or campus commute! The {model_name} is lightweight, fast-folding for metro/bus transport, and 100% puncture-proof."
            hook_ar = f"تجنب الازدحام وتكاليف المواصلات المرتفعة في تنقلاتك اليومية! سكوتر {model_name} خفيف الوزن، سريع الطي للتنقل بالحافلة والمترو، ومقاوم للثقب بنسبة 100%."

        elif any(w in t_lower for w in ["heat", "summer", "faster", "catchup", "sun", "hot", "beat", "weather"]):
            title_en = f"☀️ Beat Dubai Summer Heat: {model_name} ({price})"
            title_ar = f"☀️ تغلب على حرارة الصيف في دبي: سكوتر {model_name} ({price})"
            hook_en = f"Don't let the heat slow you down! While pneumatic tires pop on 65°C summer asphalt, Mankeel's solid honeycomb tires are 100% puncture-proof and heat-resistant."
            hook_ar = f"لا تدع حرارة الصيف تبطئ حركتك! بينما تتعرض الإطارات الهوائية للبنشر على أسفلت الصيف الحار (65 درجة)، تتميز إطارات مانكيل الصلبة بأنها مقاومة للثقب والحرارة تماماً."

        elif any(w in t_lower for w in ["community", "jvc", "motor city", "sports city", "damac", "ranches", "mudon", "delivery"]):
            title_en = f"🏡 Free Local Doorstep Delivery: {model_name}"
            title_ar = f"🏡 توصيل مجاني لباب منزلك: سكوتر {model_name}"
            hook_en = f"Need a fast, reliable e-scooter delivered directly to your villa or apartment in Dubai? We offer free doorstep delivery with in-person inspection before payment!"
            hook_ar = f"هل تبحث عن سكوتر كهربائي موثوق يصل مباشرة إلى شقتك أو فيلتك في دبي؟ نقدم توصيل مجاني لباب المنزل مع إمكانية المعاينة بنفسك قبل الدفع!"

        elif any(w in t_lower for w in ["off-road", "offroad", "power", "hill", "dirt", "suspension", "terrain", "all-terrain"]):
            title_en = f"⚡ High-Torque All-Terrain Performance: {model_name}"
            title_ar = f"⚡ أداء قوي على جميع الطرق: سكوتر {model_name}"
            hook_en = f"Conquer community gravel tracks, speed bumps, and inclines effortlessly. Engineered with dual rear suspensions and high-torque motor output."
            hook_ar = f"تغلب على المسارات الوعرة والمطبات في مجمعات دبي بسهولة. مزود بنظام تعليق مزدوج ومحرك عالي العزم."

        elif any(w in t_lower for w in ["budget", "cheap", "saving", "price", "deal", "offer", "discount"]):
            title_en = f"💰 Best Value E-Scooter Deal in Dubai: {model_name} ({price})"
            title_ar = f"💰 أفضل قيمة لسكوتر كهربائي في دبي: {model_name} ({price})"
            hook_en = f"Save 30% to 40% compared to AED 1,200+ brands! Get top-tier motor performance, 1-year local UAE warranty, and zero maintenance costs."
            hook_ar = f"وفّر 30% إلى 40% مقارنة بالعلامات التجارية الأخرى! احصل على أداء ممتاز، ضمان محلي لمدة سنة، وبدون تكاليف صيانة إطارات."

        else:
            title_en = f"⚡ Smart Dubai Mobility: {topic} - {model_name}"
            title_ar = f"⚡ اكتشف التنقل الذكي في دبي: {topic} - {model_name}"
            hook_en = f"Upgrade your daily Dubai commute with the {model_name}! Built for zero maintenance, thermal battery safety, and top value."
            hook_ar = f"طور تنقلاتك اليومية في دبي مع سكوتر {model_name}! مصمم بدون الحاجة لصيانة الإطارات، مع حماية البطارية وضمان محلي."

        # 3. Build Full Structured Content
        link_url = f"{self.website_url}/products/{model_slug}" if model_slug else self.website_url

        body_en = f"""{hook_en}

✨ Highlights & Specifications:
• {specs_en}
• 🛡️ 1-Year Local UAE Warranty & Battery Thermal Protection
• 🚫 100% Solid Puncture-Proof Honeycomb Tires (Zero flat tires)
• 🚚 FREE Doorstep Delivery & Handover across {self.delivery_areas_en}

💰 Price: {price} (VAT Included)
📲 Order Direct / View Specs: {link_url}"""

        body_ar = f"""{hook_ar}

✨ أبرز المواصفات والمميزات:
• {specs_ar}
• 🛡️ ضمان محلي في الإمارات لمدة سنة + حماية حرارية للبطارية
• 🚫 إطارات صلبة مقاومة للثقب 100% (بدون بنشر على الأسفلت الحار)
• 🚚 توصيل مجاني لباب المنزل مع المعاينة قبل الاستلام في: {self.delivery_areas_ar}

💰 السعر: {price} (شامل الضريبة)
📲 للطلب المباشر أو معرفة المواصفات: {link_url}"""

        return {
            "topic": topic,
            "title_en": title_en,
            "title_ar": title_ar,
            "body_en": body_en,
            "body_ar": body_ar,
            "target_models": [target_model]
        }
