
# import streamlit as st

# st.title("🧠 Model Training Code and Performance")

# st.markdown("""
# Explore the training code, rationale, and performance of each model (CatBoost, XGBoost, LightGBM) used in our project.
# """)

# # Define tabs
# catboost_tab, xgboost_tab, lightgbm_tab, model_choosing_Tab = st.tabs(["CatBoost","🌲 XGBoost", "💡 LightGBM Ensemble", "Model Choice Rationale and Summary"])

# --- CatBoost Tab ---
# with catboost_tab:
#     st.subheader("🐱 CatBoost Model Training")
#     st.markdown("""
# CatBoost is particularly effective for small to medium-sized datasets and handles categorical data well. It includes built-in mechanisms to deal with class imbalance using `auto_class_weights='Balanced'`, making it ideal for our dividend prediction task.
# """)
#     st.code("""
# from catboost import CatBoostClassifier

# # Define CatBoost model
# cat_model = CatBoostClassifier(
#     iterations=300,
#     learning_rate=0.05,
#     depth=6,
#     loss_function='MultiClass',
#     eval_metric='TotalF1',
#     random_seed=42,
#     verbose=0,
#     auto_class_weights='Balanced'
# )

# # Fit the model
# cat_model.fit(X_train_resampled, y_train_resampled)

# # Predict
# y_pred = cat_model.predict(X_test)
# y_pred = y_pred.flatten()

# # Decode predictions
# y_pred_decoded = [inv_label_map[p] for p in y_pred]
# y_test_decoded = [inv_label_map[t] for t in y_test]

# from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
# import matplotlib.pyplot as plt
# import seaborn as sns

# st.subheader("📊 Performance Metrics")
# report = classification_report(y_test_decoded, y_pred_decoded, output_dict=True)
# accuracy = accuracy_score(y_test_decoded, y_pred_decoded)
# st.write("**Accuracy:**", round(accuracy, 4))
# st.json(report)

# cm = confusion_matrix(y_test_decoded, y_pred_decoded, labels=[-1, 0, 1])
# fig, ax = plt.subplots(figsize=(6, 4))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
#             xticklabels=['↓ Decrease', '= Same', '↑ Increase'],
#             yticklabels=['↓ Decrease', '= Same', '↑ Increase'], ax=ax)
# ax.set_title("Confusion Matrix (CatBoost)")
# ax.set_xlabel("Predicted")
# ax.set_ylabel("Actual")
# st.pyplot(fig)
#     """, language="python")
#     st.subheader("📊 Performance Metrics:")
#     st.image("images/catboost.png", caption="Classification Report and Confusion Matrix", use_container_width=700)

# # --- LightGBM Tab ---
# with lightgbm_tab:
#     st.subheader("💡 LightGBM Ensemble Model Training")
#     st.markdown("""
# We chose a LightGBM-based ensemble with Logistic Regression and Decision Trees because it balances speed and performance, especially with class imbalance managed via SMOTE. The soft-voting ensemble helps average diverse decision boundaries for robust predictions.
# """)
#     st.code("""
# from lightgbm import LGBMClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import VotingClassifier
# from imblearn.over_sampling import SMOTE
# from collections import Counter
# import pickle, os

# models_per_industry_lgb = {}
# os.makedirs("/content/drive/MyDrive/dividend-predictor-app/models", exist_ok=True)

# for industry in industries:
#     print(f"\n⚙️ Training LightGBM ensemble for {industry}...")

#     train_ind = train[train['Industry'] == industry]
#     test_ind = test[test['Industry'] == industry]

#     X_train = train_ind[features]
#     y_train = train_ind['mapped_target']
#     X_test = test_ind[features]
#     y_test = test_ind['mapped_target']

#     if len(Counter(y_train)) < 2:
#         print(f"⚠️ Skipping {industry} — insufficient class diversity.")
#         continue

#     if min(Counter(y_train).values()) > 5:
#         smote = SMOTE(random_state=42)
#         X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
#     else:
#         X_train_resampled, y_train_resampled = X_train, y_train

#     # Create models
#     lgb_model = LGBMClassifier(class_weight='balanced', random_state=42)
#     log_model = LogisticRegression(max_iter=1000, class_weight='balanced')
#     tree_model = DecisionTreeClassifier(class_weight='balanced', max_depth=5)

#     # Voting Ensemble
#     ensemble = VotingClassifier(
#         estimators=[('lgb', lgb_model), ('lr', log_model), ('dt', tree_model)],
#         voting='soft'
#     )

#     ensemble.fit(X_train_resampled, y_train_resampled)
#     models_per_industry_lgb[industry] = ensemble

#     filename = f"/content/drive/MyDrive/dividend-predictor-app/models/lightgbm_model_{industry.lower().replace(' ', '_')}.pkl"
#     with open(filename, "wb") as f:
#         pickle.dump(ensemble, f)

#     print(f"✅ Saved {industry} model at: {filename}")

# from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
# import matplotlib.pyplot as plt
# import seaborn as sns

# y_pred = ensemble.predict(X_test)
# y_pred_decoded = [inv_label_map[p] for p in y_pred]
# y_test_decoded = [inv_label_map[t] for t in y_test]

# st.subheader("📊 Performance Metrics")
# report = classification_report(y_test_decoded, y_pred_decoded, output_dict=True)
# accuracy = accuracy_score(y_test_decoded, y_pred_decoded)
# st.write("**Accuracy:**", round(accuracy, 4))
# st.json(report)

# cm = confusion_matrix(y_test_decoded, y_pred_decoded, labels=[-1, 0, 1])
# fig, ax = plt.subplots(figsize=(6, 4))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
#             xticklabels=['↓ Decrease', '= Same', '↑ Increase'],
#             yticklabels=['↓ Decrease', '= Same', '↑ Increase'], ax=ax)
# ax.set_title(f"Confusion Matrix for {industry} (LightGBM Ensemble)")
# ax.set_xlabel("Predicted")
# ax.set_ylabel("Actual")
# st.pyplot(fig)
#     """, language="python")
#     st.subheader("📊 Performance Metrics:")
#     st.subheader("📊 1. Voting Ensemble method :")
#     st.image("images/le.png", caption="Classification Report Ensemble", use_container_width=700)
#     st.image("images/lightensemble.png", caption="Confusion Matrix Ensemble", use_container_width=700)
#     st.subheader("📊 2. Financial Sector :")
#     st.image("images/lf.png", caption="Classification Report for Financial", use_container_width=700)
#     st.image("images/lfconf.png", caption="Confusion Matrix for Financial", use_container_width=700)

# # --- XGBoost Tab (Placeholder) ---
# with xgboost_tab:
#     st.subheader("🌲 XGBoost Model Training")
#     st.markdown("""XGBoost is a gradient boosting framework that excels on structured/tabular data. It’s widely used for its speed, regularization capabilities, and scalability.""")
#     st.code("""
# from xgboost import XGBClassifier
# from imblearn.over_sampling import SMOTE
# from sklearn.metrics import classification_report, confusion_matrix
# from collections import Counter
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Map labels to 0, 1, 2 for XGBoost
# label_map = {-1: 0, 0: 1, 1: 2}
# inv_label_map = {0: -1, 1: 0, 2: 1}
# train['mapped_target'] = train['change_div'].map(label_map)
# test['mapped_target'] = test['change_div'].map(label_map)

# models_per_industry_xgb = {}

# for industry in industries:
#     print(f"\n🔍 Training XGBoost model for {industry} Industry...")

#     train_industry = train[train['Industry'] == industry]
#     test_industry = test[test['Industry'] == industry]

#     X_train = train_industry[features]
#     y_train = train_industry['mapped_target']
#     X_test = test_industry[features]
#     y_test = test_industry['mapped_target']

#     class_counts = y_train.value_counts()
#     print(f"Class distribution:\n{class_counts}")

#     if len(class_counts) < 2:
#         print(f"⚠️ Skipping {industry} — not enough class diversity.")
#         continue

#     try:
#         if min(Counter(y_train).values()) > 5:
#             smote = SMOTE(random_state=42)
#             X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
#         else:
#             print(f"⚠️ Not enough samples for SMOTE in {industry}, using unbalanced data.")
#             X_train_resampled, y_train_resampled = X_train, y_train

#         model = XGBClassifier(
#             objective='multi:softprob',
#             num_class=3,
#             eval_metric='mlogloss',
#             use_label_encoder=False,
#             learning_rate=0.05,
#             max_depth=5,
#             n_estimators=300,
#             random_state=42
#         )

#         model.fit(X_train_resampled, y_train_resampled)
#         models_per_industry_xgb[industry] = model

#         y_pred = model.predict(X_test)
#         y_pred_decoded = [inv_label_map[p] for p in y_pred]
#         y_test_decoded = [inv_label_map[t] for t in y_test]

#         print("📊 Classification Report:\n", classification_report(y_test_decoded, y_pred_decoded))
#         cm = confusion_matrix(y_test_decoded, y_pred_decoded, labels=[-1, 0, 1])
#         print("Confusion Matrix:\n", cm)

#         plt.figure(figsize=(6, 4))
#         sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
#                     xticklabels=['↓', '=', '↑'], yticklabels=['↓', '=', '↑'])
#         plt.title(f"Confusion Matrix for {industry} (XGBoost)")
#         plt.xlabel("Predicted")
#         plt.ylabel("Actual")
#         plt.tight_layout()
#         plt.show()

#     except Exception as e:
#         print(f"❌ Failed for {industry} with error: {e}")
#         continue
#     """, language="python")
#     st.subheader("📊 Performance Metrics:")
#     st.subheader("📊 1. Consumer Dictionary Sector :")
#     st.image("images/xgbc.png", caption="Classification Report for Consumer", use_container_width=700)
#     st.image("images/xgbcconf.png", caption="Confusion Matrix for Consumer", use_container_width=700)
#     st.subheader("📊 2. Energy Sector :")
#     st.image("images/xgbe.png", caption="Classification Report for Energy", use_container_width=700)
#     st.image("images/xgbeconf.png", caption="Confusion Matrix for Energy", use_container_width=700)
#     st.subheader("📊 2. Financial Sector :")
#     st.image("images/xgbf.png", caption="Classification Report for Financial", use_container_width=700)
#     st.image("images/xgbfconf.png", caption="Confusion Matrix for Financial", use_container_width=700)
#     st.subheader("📊 2. Other Sector :")
#     st.image("images/xgbo.png", caption="Classification Report for Other", use_container_width=700)
#     st.image("images/xgboconf.png", caption="Confusion Matrix for Other", use_container_width=700)

# with model_choosing_Tab:
#     st.title("🔍 Model Choice Rationale and Training Summary")

#     st.markdown("""
# In this project, we aimed to predict dividend changes using structured financial data across different industries. We selected three powerful models commonly used for tabular data: **CatBoost**, **XGBoost**, and **LightGBM**.

# Below is a summary of why we chose each model and key highlights from their training results.
# """)

#     st.header("🐱 CatBoost")
#     st.markdown("""
# - **Why CatBoost?**
#   - Handles categorical features inherently (though not used directly here).
#   - Excellent performance on small/medium-sized tabular datasets.
#   - Robust to overfitting and handles class imbalance using `auto_class_weights='Balanced'`.

# - **Training Highlights:**
#   - Iterations: 300
#   - Learning Rate: 0.05
#   - Depth: 6
#   - Evaluation Metric: Total F1
#   - auto_class_weights='Balanced' , this handles imbalance!
# """)

#     st.header("💡 LightGBM Ensemble")
#     st.markdown("""
# - **Why LightGBM Ensemble?**
#   - Fast, efficient boosting algorithm optimized for speed and memory.
#   - Paired with Logistic Regression and Decision Trees in a **soft voting ensemble** to combine strengths of linear and nonlinear learners.
#   - Uses **SMOTE** for oversampling minority classes where needed.

# - **Training Highlights:**
#   - Models: LightGBM + Logistic Regression + Decision Tree
#   - Voting: Soft
#   - Industry-specific models saved individually
# """)

#     st.header("🌲 XGBoost")
#     st.markdown("""
# - **Why XGBoost?**
#   - Highly optimized gradient boosting algorithm.
#   - Strong performance on structured/tabular data.
#   - Good regularization capabilities (L1/L2) to prevent overfitting.
# """)


import streamlit as st

st.set_page_config(page_title="Model Training Code and Performance", layout="wide")

st.title("🧠 Model Training Code and Performance")

st.markdown("""
Explore the training code, rationale, and performance of each model (CatBoost, XGBoost, LightGBM) used in our project.
""")

# Define tabs
catboost_tab, xgboost_tab, lightgbm_tab, model_choosing_Tab = st.tabs([
    "🐱 CatBoost",
    "🌲 XGBoost",
    "💡 LightGBM Ensemble",
    "📌 Model Choice Rationale and Summary"
])

with catboost_tab:
    st.subheader("🐱 CatBoost Model Training")
    st.markdown("""
CatBoost is particularly effective for small to medium-sized datasets and handles categorical data well. It includes built-in mechanisms to deal with class imbalance using `auto_class_weights='Balanced'`, making it ideal for our dividend prediction task.
""")
    st.code("""
from catboost import CatBoostClassifier

cat_model = CatBoostClassifier(
    iterations=300,
    learning_rate=0.05,
    depth=6,
    loss_function='MultiClass',
    eval_metric='TotalF1',
    random_seed=42,
    verbose=0,
    auto_class_weights='Balanced'
)

cat_model.fit(X_train_resampled, y_train_resampled)
y_pred = cat_model.predict(X_test)
y_pred = y_pred.flatten()

# Decode predictions
y_pred_decoded = [inv_label_map[p] for p in y_pred]
y_test_decoded = [inv_label_map[t] for t in y_test]
    """, language="python")
    st.image("images/catboost.png", caption="Classification Report and Confusion Matrix", use_column_width=True)

with lightgbm_tab:
    st.subheader("💡 LightGBM Ensemble Model Training")
    st.markdown("""
We chose a LightGBM-based ensemble with Logistic Regression and Decision Trees because it balances speed and performance, especially with class imbalance managed via SMOTE. The soft-voting ensemble helps average diverse decision boundaries for robust predictions.
""")
    st.code("""
from lightgbm import LGBMClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from imblearn.over_sampling import SMOTE
from collections import Counter
import pickle, os

lgb_model = LGBMClassifier(class_weight='balanced', random_state=42)
log_model = LogisticRegression(max_iter=1000, class_weight='balanced')
tree_model = DecisionTreeClassifier(class_weight='balanced', max_depth=5)
ensemble = VotingClassifier(estimators=[('lgb', lgb_model), ('lr', log_model), ('dt', tree_model)], voting='soft')
ensemble.fit(X_train_resampled, y_train_resampled)
    """, language="python")
    st.subheader("📊 1. Voting Ensemble method :")
    st.image("images/le.png", caption="Classification Report Ensemble", use_column_width=True)
    st.image("images/lightensemble.png", caption="Confusion Matrix Ensemble", use_column_width=True)
    st.subheader("📊 2. Financial Sector :")
    st.image("images/lf.png", caption="Classification Report for Financial", use_column_width=True)
    st.image("images/lfconf.png", caption="Confusion Matrix for Financial", use_column_width=True)

with xgboost_tab:
    st.subheader("🌲 XGBoost Model Training")
    st.markdown("""XGBoost is a gradient boosting framework that excels on structured/tabular data. It’s widely used for its speed, regularization capabilities, and scalability.""")
    st.code("""
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report, confusion_matrix
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

model = XGBClassifier(
    objective='multi:softprob',
    num_class=3,
    eval_metric='mlogloss',
    use_label_encoder=False,
    learning_rate=0.05,
    max_depth=5,
    n_estimators=300,
    random_state=42
)

model.fit(X_train_resampled, y_train_resampled)
y_pred = model.predict(X_test)
y_pred_decoded = [inv_label_map[p] for p in y_pred]
y_test_decoded = [inv_label_map[t] for t in y_test]
    """, language="python")
    st.subheader("📊 1. Consumer Sector :")
    st.image("images/xgbc.png", caption="Classification Report for Consumer", use_column_width=True)
    st.image("images/xgbcconf.png", caption="Confusion Matrix for Consumer", use_column_width=True)
    st.subheader("📊 2. Energy Sector :")
    st.image("images/xgbe.png", caption="Classification Report for Energy", use_column_width=True)
    st.image("images/xgbeconf.png", caption="Confusion Matrix for Energy", use_column_width=True)
    st.subheader("📊 3. Financial Sector :")
    st.image("images/xgbf.png", caption="Classification Report for Financial", use_column_width=True)
    st.image("images/xgbfconf.png", caption="Confusion Matrix for Financial", use_column_width=True)
    st.subheader("📊 4. Other Sector :")
    st.image("images/xgbo.png", caption="Classification Report for Other", use_column_width=True)
    st.image("images/xgboconf.png", caption="Confusion Matrix for Other", use_column_width=True)

with model_choosing_Tab:
    st.title("🔍 Model Choice Rationale and Training Summary")

    st.header("🐱 CatBoost")
    st.markdown("""
- **Why CatBoost?**
  - Handles categorical features inherently (though not used directly here).
  - Excellent performance on small/medium-sized tabular datasets.
  - Robust to overfitting and handles class imbalance using `auto_class_weights='Balanced'`.

- **Training Highlights:**
  - Iterations: 300
  - Learning Rate: 0.05
  - Depth: 6
  - Evaluation Metric: Total F1
  - auto_class_weights='Balanced'
""")

    st.header("💡 LightGBM Ensemble")
    st.markdown("""
- **Why LightGBM Ensemble?**
  - Fast, efficient boosting algorithm optimized for speed and memory.
  - Paired with Logistic Regression and Decision Trees in a **soft voting ensemble** to combine strengths of linear and nonlinear learners.
  - Uses **SMOTE** for oversampling minority classes where needed.

- **Training Highlights:**
  - Models: LightGBM + Logistic Regression + Decision Tree
  - Voting: Soft
  - Industry-specific models saved individually
""")

    st.header("🌲 XGBoost")
    st.markdown("""
- **Why XGBoost?**
  - Highly optimized gradient boosting algorithm.
  - Strong performance on structured/tabular data.
  - Good regularization capabilities (L1/L2) to prevent overfitting.
""")
